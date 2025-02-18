import numpy as np
import time
from tabpfn.model.preprocessing import ReshapeFeatureDistributionsStep

def test_subsample_speed():
    # Test with default subsample_features (-1) which results in no subsampling.
    print("Testing with default subsample_features (-1)")
    n_samples, n_features = 200, 100
    X = np.random.rand(n_samples, n_features)
    categorical_features = []  # no categorical features for simplicity

    step_default = ReshapeFeatureDistributionsStep(
        transform_name="safepower",
        apply_to_categorical=False,
        append_to_original=False,
        subsample_features=-1,  # default: no subsampling, use all features
        global_transformer_name=None,
        random_state=42,
    )

    t0 = time.perf_counter()
    default_result = step_default.fit_transform(X, categorical_features)
    t1 = time.perf_counter()
    step_default.transform(X)
    t2 = time.perf_counter()

    default_fit_time = t1 - t0
    default_transform_time = t2 - t1

    print(f"Default fit_transform time: {default_fit_time:.6f} sec")
    print(f"Default transform time: {default_transform_time:.6f} sec")
    print("Default transformed shape:", default_result.X.shape)

    # Now test with a huge subsample_features value.
    # To prevent blowing up memory we reduce the number of input features.
    print("\nTesting with subsample_features = 1000000")
    n_samples, n_features = 200, 10  # fewer features to keep memory usage reasonable
    X = np.random.rand(n_samples, n_features)

    step_large = ReshapeFeatureDistributionsStep(
        transform_name="safepower",
        apply_to_categorical=False,
        append_to_original=False,
        subsample_features=1000000,  # setting a huge value so nearly "no subsampling" logic is bypassed
        global_transformer_name=None,
        random_state=42,
    )

    t0 = time.perf_counter()
    large_result = step_large.fit_transform(X, categorical_features)
    t1 = time.perf_counter()
    step_large.transform(X)
    t2 = time.perf_counter()

    large_fit_time = t1 - t0
    large_transform_time = t2 - t1

    print(f"Large subsample fit_transform time: {large_fit_time:.6f} sec")
    print(f"Large subsample transform time: {large_transform_time:.6f} sec")
    print("Large subsample transformed shape:", large_result.X.shape)

if __name__ == '__main__':
    test_subsample_speed() 
