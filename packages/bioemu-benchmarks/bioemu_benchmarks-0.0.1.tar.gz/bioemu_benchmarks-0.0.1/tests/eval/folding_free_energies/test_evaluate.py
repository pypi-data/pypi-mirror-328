import numpy as np

from bioemu_benchmarks.benchmarks import Benchmark
from bioemu_benchmarks.eval.folding_free_energies.evaluate import evaluate_folding_free_energies
from bioemu_benchmarks.samples import IndexedSamples, find_samples_in_dir

TARGET_MAE = np.array([1.3885725076390523, 1.4871992468525588])


def test_evaluate_folding_free_energies(samples_path, fnc_test_data_wt):
    """Check if evaluate function works as intended."""
    sequence_samples = find_samples_in_dir(samples_path)
    indexed_samples = IndexedSamples.from_benchmark(
        Benchmark.FOLDING_FREE_ENERGIES, sequence_samples
    )

    free_energy_results = evaluate_folding_free_energies(indexed_samples, temperature_K=295)

    assert len(free_energy_results.free_energies_per_system) == 2
    assert len(free_energy_results.fnc_per_system) == 2

    # Check wild type results (mutant will be inconsistent because of modified FNC).
    results_wt = free_energy_results.free_energies_per_system[
        free_energy_results.free_energies_per_system.name == fnc_test_data_wt.test_case
    ]
    np.testing.assert_allclose(results_wt.dg_pred.values[0], fnc_test_data_wt.target_dg)
    np.testing.assert_allclose(results_wt.threshold.values[0], fnc_test_data_wt.threshold)
    np.testing.assert_allclose(results_wt.temperature.values[0], fnc_test_data_wt.temperature)

    # Check fraction native contacts.
    np.testing.assert_allclose(
        free_energy_results.fnc_per_system[fnc_test_data_wt.test_case], fnc_test_data_wt.fnc
    )

    # Perform check if metrics were computed and stored properly.
    np.testing.assert_allclose(free_energy_results.metrics.mae, TARGET_MAE)
