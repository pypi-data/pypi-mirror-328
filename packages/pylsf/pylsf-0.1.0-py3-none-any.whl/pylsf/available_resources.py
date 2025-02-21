#%%
import pandas as pd
import subprocess
from io import StringIO
from datetime import datetime

class ClusterUsageAnalyzer:
    def __init__(self, mem_threshold: float = 1.0):
        self.mem_threshold = mem_threshold
        self.last_update = None
        self.df = self._update_data()
        
    def _run_bhosts_command(self) -> str:
        """Run bhosts -gpu command and return its output"""
        try:
            result = subprocess.run(['bhosts', '-gpu'], 
                                 capture_output=True, 
                                 text=True, 
                                 check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error running bhosts command: {e}")
            return None
        
    def _update_data(self) -> pd.DataFrame:
        """Get fresh data from bhosts -gpu and process it"""
        output = self._run_bhosts_command()
        if output is None:
            return self.df if hasattr(self, 'df') else None
            
        # Read the command output as a dataframe
        df = pd.read_fwf(StringIO(output), colspecs='infer')
        df.columns = df.columns.str.strip()
        df['HOST_NAME'] = df['HOST_NAME'].ffill()
        df['MUSED'] = pd.to_numeric(df['MUSED'].str.replace('G', '').str.replace('M', 'e-3'))
        df['MRSV'] = pd.to_numeric(df['MRSV'].str.replace('G', '').str.replace('M', 'e-3'))
        
        # Calculate availability flags
        df['GPU_LOW_MEM'] = df['MUSED'] < self.mem_threshold
        df['GPU_NO_JOB'] = df['NJOBS'] < 1
        df['GPU_AVAILABLE'] = df['GPU_LOW_MEM'] & df['GPU_NO_JOB']
        df['NODE_NO_JOB'] = df.groupby('HOST_NAME').transform('all')['GPU_NO_JOB']
        df['NODE_LOW_MEM'] = df.groupby('HOST_NAME').transform('all')['GPU_LOW_MEM']
        df['NODE_AVAILABLE'] = df['NODE_LOW_MEM'] & df['NODE_NO_JOB']
        
        self.last_update = datetime.now()
        return df
    
    def refresh(self):
        """Refresh the data by running bhosts -gpu again"""
        self.df = self._update_data()
        return self
    
    def print_summary(self, detailed: bool = False):
        """Print summary of cluster usage"""
        if self.df is None:
            print("No data available - bhosts command failed")
            return
            
        available_nodes = self.df[self.df['NODE_AVAILABLE']]['HOST_NAME'].unique()
        total_nodes = self.df['HOST_NAME'].unique()
        available_gpus = self.df[self.df['GPU_AVAILABLE']].shape[0]
        total_gpus = self.df.shape[0]

        print("\n=== Cluster Resource Summary ===")
        print(f"Last Updated: {self.last_update.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Nodes fully Available: {len(available_nodes)}/{len(total_nodes)} "
              f"({100*len(available_nodes)/len(total_nodes):.1f}%)")
        print(f"GPUs fully Available:  {available_gpus}/{total_gpus} "
              f"({100*available_gpus/total_gpus:.1f}%)")

        if not detailed:
            return

        if len(available_nodes) > 0:
            print("\nFully Available Nodes:")
            for node in sorted(available_nodes):
                print(f"  - {node}")

        partial_nodes = self.df[(self.df['GPU_AVAILABLE']) & ~self.df['NODE_AVAILABLE']]['HOST_NAME'].unique()
        if len(partial_nodes) > 0:
            print("\nPartially Available Nodes:")
            for node in sorted(partial_nodes):
                node_gpus = self.df[self.df['HOST_NAME'] == node]
                free_gpus = node_gpus[node_gpus['GPU_AVAILABLE']]['GPU_ID'].tolist()
                print(f"  - {node}: GPUs {free_gpus}")
        print()

if __name__ == "__main__":
    analyzer = ClusterUsageAnalyzer()

    while True:
        analyzer.refresh().print_summary()
 