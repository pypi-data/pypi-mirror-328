import numpy as np
import time
from sklearn.preprocessing import QuantileTransformer

def test_quantile_transformer_speed():
    # Use a dataset with many samples so that default subsampling is active.
    n_samples = 200_000  # more than the default subsample limit (typically 100000)
    n_features = 100
    n_quantiles = 10_000
    X = np.random.rand(n_samples, n_features)

    n_runs = 5
    default_times = []
    large_times = []

    for run in range(n_runs):
        print(f"\nRun {run + 1}/{n_runs}")

        # Test with subsample explicitly set
        print("\nTesting QuantileTransformer with subsample=100_000")
        qt_large = QuantileTransformer(subsample=100_000, random_state=42, n_quantiles=n_quantiles)
        t0 = time.perf_counter()
        X_trans_large = qt_large.fit_transform(X)
        X_trans_large_2 = qt_large.transform(X)
        t1 = time.perf_counter()
        large_time = t1 - t0
        large_times.append(large_time)
        print(f"QuantileTransformer (subsample=100_000) fit_transform time: {large_time:.6f} sec")
        print("Transformed shape:", X_trans_large.shape)
        
        # Test with default settings
        print("Testing QuantileTransformer with default subsample parameter")
        qt_default = QuantileTransformer(random_state=42, n_quantiles=n_quantiles)
        t0 = time.perf_counter()
        X_trans_default = qt_default.fit_transform(X)
        X_trans_default_2 = qt_default.transform(X)
        t1 = time.perf_counter()
        default_time = t1 - t0
        default_times.append(default_time)
        print(f"Default QuantileTransformer fit_transform time: {default_time:.6f} sec")
        print("Transformed shape:", X_trans_default.shape)

    # Print summary statistics
    print("\nSummary Statistics:")
    print(f"Default QuantileTransformer:")
    print(f"  Average time: {np.mean(default_times):.6f} sec")
    print(f"  Std dev: {np.std(default_times):.6f} sec")
    print(f"  Times: {[f'{t:.6f}' for t in default_times]}")
    
    print(f"\nQuantileTransformer (subsample=100_000):")
    print(f"  Average time: {np.mean(large_times):.6f} sec")
    print(f"  Std dev: {np.std(large_times):.6f} sec")
    print(f"  Times: {[f'{t:.6f}' for t in large_times]}")

if __name__ == '__main__':
    test_quantile_transformer_speed() 
