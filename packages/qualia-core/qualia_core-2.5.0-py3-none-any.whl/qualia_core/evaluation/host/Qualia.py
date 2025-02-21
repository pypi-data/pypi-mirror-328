from __future__ import annotations

import concurrent.futures
import logging
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import numpy.typing

from qualia_core.evaluation import Stats
from qualia_core.evaluation.Evaluator import Evaluator
from qualia_core.typing import TYPE_CHECKING

if TYPE_CHECKING:
    from torch.types import Number  # noqa: TCH002

    from qualia_core.dataaugmentation.DataAugmentation import DataAugmentation  # noqa: TCH001
    from qualia_core.datamodel.RawDataModel import RawDataModel  # noqa: TCH001
    from qualia_core.learningframework.LearningFramework import LearningFramework  # noqa: TCH001

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

logger = logging.getLogger(__name__)

@dataclass
class Result:
    metrics: dict[str, float]
    time: float

class Qualia(Evaluator):
    """Custom evaluation loop for Qualia host implementations like Qualia-CodeGen Linux example."""

    def __init__(self, chunks: int | None = None) -> None:
        super().__init__()
        self.__deploydir = Path('out')/'deploy'/'Linux'
        self.__chunks = chunks

    def _float_to_hex(self, arr: numpy.typing.NDArray[Any]) -> numpy.typing.NDArray[np.str_]:
        def float_to_hex(x: Number) -> str:
            return float(x).hex()
        return np.vectorize(float_to_hex)(arr)

    def _run_on_split(self,  # noqa: PLR0913
                       csvdir: Path,
                       tag: str,
                       i: int,
                       test_x: numpy.typing.NDArray[Any],
                       test_y: numpy.typing.NDArray[Any]) -> Result:
        np.savetxt(csvdir/f'testX_{i}.csv', self._float_to_hex(test_x), delimiter=',', fmt='%s')
        np.savetxt(csvdir/f'testY_{i}.csv', self._float_to_hex(test_y), delimiter=',', fmt='%s')

        cmd = [str(self.__deploydir/tag/'Linux'), str(csvdir/f'testX_{i}.csv'), str(csvdir/f'testY_{i}.csv')]
        logger.info('%d Running: %s', i, ' '.join(cmd))

        tstart = time.time() # Start timer
        res = subprocess.run(cmd, # noqa: S603 command line is safe
                             capture_output=True,
                             text=True)
        tstop = time.time() # Stop timer

        if res.stdout:
            logger.info('%d stdout: %s', i, res.stdout)
        if res.stderr:
            logger.info('%d stderr: %s', i, res.stderr)

        # Extract one metric per line of stderr
        metrics_str = dict(line.split('=') for line in res.stderr.splitlines())
        # Convert metrics value from string to float
        metrics = {name: float(value) for name, value in metrics_str.items()}

        return Result(metrics, (tstop - tstart))

    @override
    def evaluate(self,
                 framework: LearningFramework[Any],
                 model_kind: str,
                 dataset: RawDataModel,
                 target: str,
                 tag: str,
                 limit: int | None = None,
                 dataaugmentations: list[DataAugmentation] | None = None) -> Stats:
        test_x = dataset.sets.test.x
        test_y = dataset.sets.test.y

        # Apply evaluation "dataaugmentations" to dataset
        if dataaugmentations is not None:
            for da in dataaugmentations:
                if da.evaluate:
                    test_x, test_y = framework.apply_dataaugmentation(da, test_x, test_y)

        # create log directory
        (Path('logs')/'evaluate'/target).mkdir(parents=True, exist_ok=True)

        # create data CSV dir
        csvdir = Path('out')/'data'/dataset.name/'csv'
        csvdir.mkdir(parents=True, exist_ok=True)

        # Flatten test vectors
        test_x = test_x.reshape((test_x.shape[0], -1))

        if limit:
            test_x = test_x[:limit]
            test_y = test_y[:limit]

        test_vector_count = test_y.shape[0]

        # Split test into chunks
        cpu = self.__chunks if self.__chunks is not None else os.cpu_count()
        chunks = cpu if cpu is not None else 2
        test_x = np.array_split(test_x, chunks)
        test_y = np.array_split(test_y, chunks)

        with concurrent.futures.ProcessPoolExecutor(max_workers=chunks) as executor:
            futures = [executor.submit(self._run_on_split, csvdir, tag, i, x, y) for i, (x, y) in enumerate(zip(test_x, test_y))]
            results = [f.result() for f in futures]

        avg_time = sum(r.time for r in results) / test_vector_count

        # Reduce metrics over all results
        metrics: dict[str, float] = {}
        for r, y in zip(results, test_y):
            for name, value in r.metrics.items():
                if name not in metrics:
                    metrics[name] = value * len(y)
                else:
                    metrics[name] += value * len(y)
        metrics = {name: value / test_vector_count for name, value in metrics.items()}

        return Stats(avg_time=avg_time, metrics=metrics, accuracy=metrics.get('acc', -1))

        # avg it/secs
        # ram usage
        # rom usage
        # cpu type
        # cpu model
        # cpu freq
        # accuracy
        # power consumption
