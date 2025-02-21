from .mainClass import *
from .lossFunction import MeanSquaredError


import cmath
from typing import List, Tuple

class SpectralConvergence(Distance):

    def __init__(self) -> None:
        super().__init__()
        self.type='sound'

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        """
        Compute the Spectral Convergence between two signals.

        :param signal1: The first signal as a list of floats.
        :param signal2: The second signal as a list of floats.
        :return: The spectral convergence between the two signals as a float.
        """
        # Compute the FFT for both signals
        fft1: List[complex] = Sound().FFT(signal1)
        fft2: List[complex] = Sound().FFT(signal2)

        # Compute magnitudes of the spectrums
        mag1: List[float] = Sound.magnitude(fft1)
        mag2: List[float] = Sound.magnitude(fft2)

        # Ensure both spectrums are of the same length
        if len(mag1) != len(mag2):
            raise ValueError("Both signals must have the same length.")

        # Compute the Spectral Convergence
        numerator: float = sum(abs(m1 - m2) for m1, m2 in zip(mag1, mag2))
        denominator: float = sum(mag1)

        # To avoid division by zero
        if denominator == 0:
            return float('inf')

        return numerator / denominator

import math
import cmath

class MFCCProcessor(Distance):
    def __init__(self, sample_rate: int = 16000, n_mfcc: int = 13, n_fft: int = 2048, n_mels: int = 26)-> None:
        super().__init__()
        self.type='sound'

        self.sample_rate = sample_rate
        self.n_mfcc = n_mfcc
        self.n_fft = n_fft
        self.n_mels = n_mels

    def _mel_to_hz(self, mel: float) -> float:
        return 700 * (10 ** (mel / 2595) - 1)

    def _hz_to_mel(self, hz: float) -> float:
        return 2595 * math.log10(1 + hz / 700)

    def _mel_filterbank(self) -> List[List[float]]:
        low_freq_mel = self._hz_to_mel(0)
        high_freq_mel = self._hz_to_mel(self.sample_rate / 2)
        mel_points = [low_freq_mel + i * (high_freq_mel - low_freq_mel) / (self.n_mels + 1) for i in range(self.n_mels + 2)]
        hz_points = [self._mel_to_hz(mel) for mel in mel_points]
        bin_points = [int(round((self.n_fft + 1) * hz / self.sample_rate)) for hz in hz_points]

        fbank = [[0.0] * (self.n_fft // 2 + 1) for _ in range(self.n_mels)]
        for m in range(1, self.n_mels + 1):
            f_m_minus = bin_points[m - 1]
            f_m = bin_points[m]
            f_m_plus = bin_points[m + 1]

            for k in range(f_m_minus, f_m):
                fbank[m-1][k] = (k - f_m_minus) / (f_m - f_m_minus)
            for k in range(f_m, f_m_plus):
                fbank[m-1][k] = (f_m_plus - k) / (f_m_plus - f_m)

        return fbank

    def _dct(self, x: List[float]) -> List[float]:
        N = len(x)
        y = [0.0] * N
        for k in range(N):
            for n in range(N):
                y[k] += x[n] * math.cos(math.pi * k * (2 * n + 1) / (2 * N))
        return y

    def compute(self, signal1: List[float], signal2: List[float]) -> Tuple[List[List[float]], List[List[float]]]:
        """
        Calcule les MFCC pour deux signaux audio.

        Args:
            signal1 (List[float]): Premier signal audio.
            signal2 (List[float]): Deuxième signal audio.

        Returns:
            Tuple[List[List[float]], List[List[float]]]: MFCC des deux signaux.
        """
        def process_signal(signal: List[float]) -> List[List[float]]:
            # Pré-accentuation
            pre_emphasis = 0.97
            emphasized_signal = [signal[i] - pre_emphasis * signal[i-1] for i in range(1, len(signal))]

            # Fenêtrage
            frame_length = self.n_fft
            frame_step = frame_length // 2
            frames = [emphasized_signal[i:i+frame_length] for i in range(0, len(emphasized_signal) - frame_length + 1, frame_step)]

            # Appliquer la fenêtre de Hamming
            hamming = [0.54 - 0.46 * math.cos(2 * math.pi * i / (frame_length - 1)) for i in range(frame_length)]
            windowed_frames = [[frame[i] * hamming[i] for i in range(len(frame))] for frame in frames]

            # FFT
            magnitude_frames = [[abs(x) for x in Sound().FFT(frame)] for frame in windowed_frames]

            # Mel filterbank
            mel_fb = self._mel_filterbank()
            mel_spectrum = [[sum(m * f for m, f in zip(mel_filter, frame[:len(mel_filter)])) for mel_filter in mel_fb] for frame in magnitude_frames]

            # Log
            log_mel_spectrum = [[math.log(x + 1e-8) for x in frame] for frame in mel_spectrum]

            # DCT
            mfcc = [self._dct(frame)[:self.n_mfcc] for frame in log_mel_spectrum]

            return mfcc

        mfcc1 = process_signal(signal1)
        mfcc2 = process_signal(signal2)

        return mfcc1, mfcc2

    def compare_mfcc(self, signal1: List[float], signal2: List[float]) -> List[float]:
        """
        Calcule et compare les MFCC de deux signaux audio.

        Args:
            signal1 (List[float]): Premier signal audio.
            signal2 (List[float]): Deuxième signal audio.

        Returns:
            List[float]: Distance euclidienne moyenne entre les MFCC des deux signaux.
        """
        mfcc1, mfcc2 = self.compute(signal1, signal2)

        # Assurez-vous que les deux MFCC ont le même nombre de trames
        min_frames = min(len(mfcc1), len(mfcc2))
        mfcc1 = mfcc1[:min_frames]
        mfcc2 = mfcc2[:min_frames]

        # Calculez la distance euclidienne moyenne
        distances = []
        for frame1, frame2 in zip(mfcc1, mfcc2):
            distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(frame1, frame2)))
            distances.append(distance)

        return sum(distances) / len(distances)
        
    def example(self):

      # Générer les signaux de test
      test_signal1, test_signal2 = Sound.generate_test_signals()

      # Afficher les 10 premiers échantillons de chaque signal
      print("10 premiers échantillons du signal 1:", test_signal1[:10])
      print("10 premiers échantillons du signal 2:", test_signal2[:10])

      print(f"Nombre d'échantillons dans chaque signal: {len(test_signal1)}")
      print(f"Fréquence d'échantillonnage: 16000 Hz")
      print(f"Durée de chaque signal: 1.0 seconde")


      # Créer une instance de MFCCProcessor
      processor = MFCCProcessor()

      # Calculer les MFCC pour les deux signaux
      mfcc1, mfcc2 = processor.compute(test_signal1, test_signal2)

      # Comparer les MFCC
      distance = processor.compare_mfcc(test_signal1, test_signal2)

      print(f"Nombre de trames MFCC pour chaque signal: {len(mfcc1)}")
      print(f"Nombre de coefficients MFCC par trame: {len(mfcc1[0])}")
      print(f"Distance moyenne entre les MFCC des deux signaux: {distance}")

      # Afficher les premiers coefficients MFCC de la première trame pour chaque signal
      print("Premiers coefficients MFCC du signal 1:", mfcc1[0][:5])
      print("Premiers coefficients MFCC du signal 2:", mfcc2[0][:5])
      
#claude ai fft
'''
from typing import List
import cmath

class SignalProcessor(Distance):

    def __init__(self) -> None:
        super().__init__()
        self.type='sound'

    def _fft(self, signal: List[float]) -> List[complex]:
        """
        Calcule la Transformée de Fourier Rapide (FFT) d'un signal sonore.

        Args:
            signal (List[float]): Le signal d'entrée sous forme de liste de nombres flottants.

        Returns:
            List[complex]: La FFT du signal sous forme de liste de nombres complexes.
        """
        n = len(signal)
        if n <= 1:
            return signal

        # Diviser le signal en pair et impair
        even = self._fft(signal[0::2])
        odd = self._fft(signal[1::2])

        # Combiner
        combined = [0] * n
        for k in range(n // 2):
            t = cmath.exp(-2j * cmath.pi * k / n) * odd[k]
            combined[k] = even[k] + t
            combined[k + n // 2] = even[k] - t

        return combined

    @staticmethod
    def pad_to_power_of_two(signal: List[float]) -> List[float]:
        """
        Complète le signal avec des zéros pour atteindre une longueur qui est une puissance de 2.

        Args:
            signal (List[float]): Le signal d'entrée.

        Returns:
            List[float]: Le signal complété.
        """
        n = 1
        while n < len(signal):
            n *= 2
        return signal + [0.0] * (n - len(signal))

processor = SignalProcessor()
signal1 = [0.1, 0.2, 0.3, 0.4, 0.5]  # exemple de signal
signal2 = [0.2, 0.3, 0.4, 0.5, 0.6]  # autre exemple de signal
fft_difference = processor._fft(signal1)
print(fft_difference)
'''
##############"
import math
from typing import List

class PowerSpectralDensityDistance(Distance):

    def __init__(self, sample_rate: int=16000) -> None:
        super().__init__()
        self.type='sound'

        self.sample_rate = sample_rate

    def _psd(self, signal: List[float]) -> List[float]:
        fft_result = Sound().FFT(signal)
        magnitude_spectrum = [abs(freq) ** 2 for freq in fft_result[:len(fft_result) // 2]]
        return magnitude_spectrum

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        psd1 = self._psd(signal1)
        psd2 = self._psd(signal2)

        distance = sum((psd1[i] - psd2[i]) ** 2 for i in range(min(len(psd1), len(psd2))))
        return math.sqrt(distance)
    def example(self):
      test_signal1, test_signal2 = Sound.generate_test_signals()
      psd_calculator = PowerSpectralDensityDistance(sample_rate=16000)
      psd_distance = psd_calculator.compute(test_signal1, test_signal2)
      print("PSD Distance:", psd_distance)
      
import math
from typing import List

class CrossCorrelation(Distance):

    def __init__(self, sample_rate: int=16000) -> None:
        super().__init__()
        self.type='sound'

        self.sample_rate: int = sample_rate

    def _mean(self, signal: List[float]) -> float:
        return sum(signal) / len(signal)

    def _normalize(self, signal: List[float]) -> List[float]:
        mean_value: float = self._mean(signal)
        return [x - mean_value for x in signal]

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        signal1_normalized: List[float] = self._normalize(signal1)
        signal2_normalized: List[float] = self._normalize(signal2)

        numerator: float = sum(signal1_normalized[i] * signal2_normalized[i] for i in range(min(len(signal1_normalized), len(signal2_normalized))))
        denominator_signal1: float = math.sqrt(sum(x ** 2 for x in signal1_normalized))
        denominator_signal2: float = math.sqrt(sum(x ** 2 for x in signal2_normalized))

        denominator: float = denominator_signal1 * denominator_signal2

        return numerator / denominator if denominator != 0 else 0.0
        
#ai claude

from typing import List, Tuple
import math
import cmath

class PhaseDifferenceCalculator(Distance):

    def __init__(self, sample_rate: int=16000, window_size: int= 1024, hop_size: int=512) -> None:
        """
        Initialise le calculateur de différence de phase.

        Args:
            sample_rate (int): Taux d'échantillonnage des signaux.
            window_size (int): Taille de la fenêtre pour l'analyse.
            hop_size (int): Taille du saut entre les fenêtres successives.
        """
        super().__init__()
        self.type='sound'

        self.sample_rate: int = sample_rate
        self.window_size: int = window_size
        self.hop_size: int = hop_size


    '''
    def _fft(self, signal: List[float]) -> List[complex]:
        """
        Calcule la Transformée de Fourier Rapide (FFT) du signal.

        Args:
            signal (List[float]): Signal d'entrée.

        Returns:
            List[complex]: FFT du signal.
        """
        n: int = len(signal)
        if n <= 1:
            return signal
        even: List[complex] = self._fft(signal[0::2])
        odd: List[complex] = self._fft(signal[1::2])
        combined: List[complex] = [0] * n
        for k in range(n // 2):
            t: complex = cmath.exp(-2j * math.pi * k / n) * odd[k]
            combined[k] = even[k] + t
            combined[k + n // 2] = even[k] - t
        return combined
    '''
    def compute(self, signal1: List[float], signal2: List[float]) -> List[float]:
        """
        Calcule la différence de phase entre deux signaux.

        Args:
            signal1 (List[float]): Premier signal.
            signal2 (List[float]): Deuxième signal.

        Returns:
            List[float]: Différence de phase pour chaque segment.
        """
        if len(signal1) != len(signal2):
            raise ValueError("Les signaux doivent avoir la même longueur")

        phase_differences: List[float] = []
        num_segments: int = (len(signal1) - self.window_size) // self.hop_size + 1

        for i in range(num_segments):
            start: int = i * self.hop_size
            end: int = start + self.window_size

            segment1: List[float] = Sound._apply_window(signal1[start:end])
            segment2: List[float] = Sound._apply_window(signal2[start:end])

            fft1: List[complex] = Sound().FFT(segment1)
            fft2: List[complex] = Sound().FFT(segment2)

            phase_diff: float = 0
            for f1, f2 in zip(fft1, fft2):
                if abs(f1) > 1e-6 and abs(f2) > 1e-6:  # Éviter la division par zéro
                    phase1: float = cmath.phase(f1)
                    phase2: float = cmath.phase(f2)
                    diff: float = phase2 - phase1
                    # Normaliser la différence de phase entre -pi et pi
                    phase_diff += (diff + math.pi) % (2 * math.pi) - math.pi

            phase_differences.append(phase_diff / len(fft1))

        return phase_differences

    def get_time_axis(self) -> List[float]:
        """
        Génère l'axe temporel pour les différences de phase calculées.

        Returns:
            List[float]: Axe temporel en secondes.
        """
        num_segments: int = len(self.compute([0] * self.window_size, [0] * self.window_size))
        return [i * self.hop_size / self.sample_rate for i in range(num_segments)]

    def analyze_signals(self, signal1: List[float], signal2: List[float]) -> Tuple[List[float], List[float]]:
        """
        Analyse deux signaux et retourne la différence de phase et l'axe temporel.

        Args:
            signal1 (List[float]): Premier signal.
            signal2 (List[float]): Deuxième signal.

        Returns:
            Tuple[List[float], List[float]]: Différence de phase et axe temporel.
        """
        phase_diff: List[float] = self.compute(signal1, signal2)
        time_axis: List[float] = self.get_time_axis()
        return phase_diff, time_axis
        
    def example(self):
      # Paramètres
      sample_rate: int = 44100  # Hz
      window_size: int = 1024   # échantillons
      hop_size: int = 512       # échantillons

      # Créer une instance du calculateur
      calculator: PhaseDifferenceCalculator = PhaseDifferenceCalculator(sample_rate, window_size, hop_size)

      # Supposons que nous ayons deux signaux signal1 et signal2
      signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
      signal2: List[float] = [0.1 * math.sin(2 * math.pi * 880 * t / 16000) for t in range(16000)]

      # Analyser les signaux
      phase_differences: List[float]
      time_axis: List[float]
      phase_differences, time_axis = calculator.analyze_signals(signal1, signal2)

      # Afficher les résultats
      print("Différences de phase:", phase_differences[:10])  # Affiche les 10 premières valeurs
      print("Axe temporel:", time_axis[:10])  # Affiche les 10 premières valeurs
      
from typing import List
import math

class TimeLagDistance(Distance):

    def __init__(self, sample_rate: int=16000) -> None:
        super().__init__()
        self.type='sound'

        self.sample_rate: int = sample_rate

    def _cross_correlation(self, signal1: List[float], signal2: List[float], lag: int) -> float:
        n: int = len(signal1)
        if lag > 0:
            shifted_signal2: List[float] = [0] * lag + signal2[:-lag]
        else:
            shifted_signal2: List[float] = signal2[-lag:] + [0] * (-lag)

        return sum(signal1[i] * shifted_signal2[i] for i in range(n))

    def compute(self, signal1: List[float], signal2: List[float], max_lag: int) -> int:
        best_lag: int = 0
        best_correlation: float = -float('inf')

        for lag in range(-max_lag, max_lag + 1):
            correlation: float = self._cross_correlation(signal1, signal2, lag)
            if correlation > best_correlation:
                best_correlation = correlation
                best_lag = lag

        return best_lag
    def example(self):
      signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
      signal2: List[float] = [0.1 * math.sin(2 * math.pi * 440 * (t - 100) / 16000) for t in range(16000)]  # signal2 is shifted

      time_lag_calculator = TimeLagDistance(sample_rate=16000)

      best_lag: int = time_lag_calculator.compute(signal1, signal2, max_lag=500)

      print("Optimal time lag:", best_lag)
      
from typing import List

class PESQ(Distance):

    def __init__(self, sample_rate: int=16000) -> None:
        super().__init__()
        self.type='sound'

        self.sample_rate: int = sample_rate

    def _preprocess(self, signal: List[float]) -> List[float]:
        # Placeholder preprocessing steps: normalization and filtering
        max_val: float = max(abs(x) for x in signal)
        return [x / max_val for x in signal] if max_val != 0 else signal

    def _compare_signals(self, reference: List[float], degraded: List[float]) -> float:
        # Placeholder function to simulate signal comparison
        mse: float = sum((reference[i] - degraded[i]) ** 2 for i in range(min(len(reference), len(degraded))))
        return mse / len(reference)

    def compute(self, reference_signal: List[float], degraded_signal: List[float]) -> float:
        reference_processed: List[float] = self._preprocess(reference_signal)
        degraded_processed: List[float] = self._preprocess(degraded_signal)

        comparison_score: float = self._compare_signals(reference_processed, degraded_processed)

        # Placeholder formula for PESQ score (the actual PESQ model is more complex)
        pesq_score: float = 4.5 - comparison_score  # 4.5 is the best score in PESQ scale

        return max(1.0, min(pesq_score, 4.5))  # PESQ scores typically range between 1.0 and 4.5
        
        
import cmath
from typing import List

class LogSpectralDistance(Distance):

    def __init__(self, sample_rate: int=16000) -> None:
        super().__init__()
        self.type='sound'

        self.sample_rate: int = sample_rate

    def _log_magnitude_spectrum(self, signal: List[float]) -> List[float]:
        fft_result: List[complex] = Sound().FFT(signal)
        return [20 * math.log10(abs(x)) if abs(x) != 0 else 0 for x in fft_result]

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        log_spectrum1: List[float] = self._log_magnitude_spectrum(signal1)
        log_spectrum2: List[float] = self._log_magnitude_spectrum(signal2)

        # Calculate the squared differences between the log-magnitude spectra
        squared_diffs: List[float] = [(log_spectrum1[i] - log_spectrum2[i]) ** 2 for i in range(min(len(log_spectrum1), len(log_spectrum2)))]

        # Compute the LSD value
        mean_squared_diff: float = sum(squared_diffs) / len(squared_diffs)
        return math.sqrt(mean_squared_diff)
        
import math
from typing import List

class BarkSpectralDistortion(Distance):

    def __init__(self, sample_rate: int=16000) -> None:
        super().__init__()
        self.type='sound'

        self.sample_rate: int = sample_rate

    def _bark_scale(self, freq: float) -> float:
        return 13 * math.atan(0.00076 * freq) + 3.5 * math.atan((freq / 7500) ** 2)

    def _compute_bark_spectrum(self, signal: List[float]) -> List[float]:
        fft_result: List[complex] = Sound().FFT(signal)
        N: int = len(fft_result)
        bark_spectrum: List[float] = [0.0] * N

        for i in range(N):
            freq: float = i * (self.sample_rate / N)
            bark_freq: float = self._bark_scale(freq)
            magnitude: float = abs(fft_result[i])
            bark_spectrum[i] = 20 * math.log10(magnitude) if magnitude != 0 else 0

        return bark_spectrum

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        bark_spectrum1: List[float] = self._compute_bark_spectrum(signal1)
        bark_spectrum2: List[float] = self._compute_bark_spectrum(signal2)

        squared_diffs: List[float] = [(bark_spectrum1[i] - bark_spectrum2[i]) ** 2 for i in range(min(len(bark_spectrum1), len(bark_spectrum2)))]

        mean_squared_diff: float = sum(squared_diffs) / len(squared_diffs)
        return math.sqrt(mean_squared_diff)

import math
from typing import List

class ItakuraSaitoDistance(Distance):

    def __init__(self) -> None:
        super().__init__()
        self.type='sound'

    def _power_spectrum(self, signal: List[float]) -> List[float]:
        N: int = len(signal)
        power_spectrum: List[float] = [0.0] * N

        for i in range(N):
            power_spectrum[i] = signal[i] ** 2
        
        return power_spectrum

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        if len(signal1) != len(signal2):
            raise ValueError("Both signals must have the same length.")

        power_spectrum1: List[float] = self._power_spectrum(signal1)
        power_spectrum2: List[float] = self._power_spectrum(signal2)
        
        is_distance: float = 0.0
        for ps1, ps2 in zip(power_spectrum1, power_spectrum2):
            if ps2 > 0:
                is_distance += (ps1 / ps2) - math.log(ps1 / ps2) - 1
        
        return is_distance
        
import math
from typing import List

class SignalToNoiseRatio(Distance):

    def __init__(self) -> None:
        super().__init__()
        self.type='sound'

    def _power(self, signal: List[float]) -> float:
        power: float = sum(s ** 2 for s in signal) / len(signal)
        return power

    def compute(self, signal: List[float], noise: List[float]) -> float:
        if len(signal) != len(noise):
            raise ValueError("Signal and noise must have the same length.")

        signal_power: float = self._power(signal)
        noise_power: float = self._power(noise)

        if noise_power == 0:
            raise ValueError("Noise power is zero, cannot compute SNR.")

        snr: float = 10 * math.log10(signal_power / noise_power)
        return snr


import math

class PeakSignalToNoiseRatio(Distance):

    def __init__(self) -> None:
        super().__init__()
        self.type='sound'

    def compute(self, signal1: List[float], signal2: List[float], max_signal_value: float) -> float:
        mse: float = MeanSquaredError().compute(signal1, signal2)
        if mse == 0:
            return float('inf')  # Signals are identical

        psnr: float = 10 * math.log10(max_signal_value ** 2 / mse)
        return psnr
        
    def example(self):
      signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
      signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

      max_signal_value: float = 1.0  # Maximum possible value for a normalized signal

      psnr_value: float = self.compute(signal1, signal2, max_signal_value)

      print("Peak Signal-to-Noise Ratio (PSNR):", psnr_value)

class EnergyDistance(Distance):

    def __init__(self) -> None:
        super().__init__()
        self.type='sound'

    def _energy(self, signal: List[float]) -> float:
        energy: float = sum(s ** 2 for s in signal)
        return energy

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        if len(signal1) != len(signal2):
            raise ValueError("Both signals must have the same length.")

        energy1: float = self._energy(signal1)
        energy2: float = self._energy(signal2)

        energy_distance: float = abs(energy1 - energy2)
        return energy_distance
        
class EnvelopeCorrelation(Distance):

    def __init__(self) -> None:
        super().__init__()
        self.type='sound'

    def _envelope(self, signal: List[float]) -> List[float]:
        # Approximation of the envelope using the absolute value of the signal
        envelope: List[float] = [abs(s) for s in signal]
        return envelope

    def _mean(self, data: List[float]) -> float:
        return sum(data) / len(data)

    def _correlation(self, envelope1: List[float], envelope2: List[float]) -> float:
        mean1: float = self._mean(envelope1)
        mean2: float = self._mean(envelope2)

        numerator: float = sum((e1 - mean1) * (e2 - mean2) for e1, e2 in zip(envelope1, envelope2))
        denominator: float = math.sqrt(sum((e1 - mean1) ** 2 for e1 in envelope1) * sum((e2 - mean2) ** 2 for e2 in envelope2))

        if denominator == 0:
            return 0.0  # No correlation if denominator is zero

        return numerator / denominator

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        if len(signal1) != len(signal2):
            raise ValueError("Both signals must have the same length.")

        envelope1: List[float] = self._envelope(signal1)
        envelope2: List[float] = self._envelope(signal2)

        correlation: float = self._correlation(envelope1, envelope2)
        return correlation
        
class ZeroCrossingRateDistance(Distance):

    def __init__(self) -> None:
        super().__init__()
        self.type='sound'

    def _zero_crossing_rate(self, signal: List[float]) -> float:
        zero_crossings: int = 0
        for i in range(1, len(signal)):
            if (signal[i - 1] > 0 and signal[i] < 0) or (signal[i - 1] < 0 and signal[i] > 0):
                zero_crossings += 1

        zcr: float = zero_crossings / len(signal)
        return zcr

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        if len(signal1) != len(signal2):
            raise ValueError("Both signals must have the same length.")

        zcr1: float = self._zero_crossing_rate(signal1)
        zcr2: float = self._zero_crossing_rate(signal2)

        zcr_distance: float = abs(zcr1 - zcr2)
        return zcr_distance
        
class CochleagramDistance(Distance):

    def __init__(self, num_bands: int = 40)-> None:
        super().__init__()
        self.type='sound'

        self.num_bands: int = num_bands

    def _bandpass_filter(self, signal: List[float], band_index: int, total_bands: int) -> List[float]:
        # Simplified bandpass filter approximation
        filtered_signal: List[float] = [0.0] * len(signal)
        band_width: float = 0.5 / total_bands
        center_freq: float = (band_index + 0.5) * band_width
        for i in range(len(signal)):
            filtered_signal[i] = signal[i] * center_freq  # Simplified filter effect
        return filtered_signal

    def _cochleagram(self, signal: List[float]) -> List[List[float]]:
        cochleagram: List[List[float]] = []
        for band in range(self.num_bands):
            band_signal: List[float] = self._bandpass_filter(signal, band, self.num_bands)
            cochleagram.append(band_signal)
        return cochleagram

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        if len(signal1) != len(signal2):
            raise ValueError("Both signals must have the same length.")

        cochlea1: List[List[float]] = self._cochleagram(signal1)
        cochlea2: List[List[float]] = self._cochleagram(signal2)

        distance: float = Sound._mean_squared_error(cochlea1, cochlea2)
        return distance


from typing import List
import math

class ChromagramDistance(Distance):

    def __init__(self, num_bins: int = 12) -> None:
        super().__init__()
        self.type='sound'

        self.num_bins: int = num_bins

    def _frequency_to_bin(self, frequency: float) -> int:
        # Simple mapping of frequency to chroma bin
        if frequency>0:
           bin_index: int = int((12 * math.log2(frequency / 440.0) + 69) % 12)
           return bin_index
        else:
           return 0


    def _compute_chromagram(self, signal: List[float]) -> List[float]:
        chroma: List[float] = [0.0] * self.num_bins
        for sample in signal:
            # Simplified frequency estimation from signal sample (placeholder)
            frequency: float = abs(sample) * 1000.0
            bin_index: int = self._frequency_to_bin(frequency)
            chroma[bin_index] += 1

        # Normalize chromagram
        total_count: float = sum(chroma)
        if total_count > 0:
            chroma = [count / total_count for count in chroma]

        return chroma

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        if len(signal1) != len(signal2):
            raise ValueError("Both signals must have the same length.")

        chroma1: List[float] = self._compute_chromagram(signal1)
        chroma2: List[float] = self._compute_chromagram(signal2)

        distance: float = MeanSquaredError().compute(chroma1, chroma2)
        return distance

import cmath

class SpectrogramDistance(Distance):

    def __init__(self, window_size: int = 256, overlap: int = 128) -> None:
        super().__init__()
        self.type='sound'

        self.window_size: int = window_size
        self.overlap: int = overlap

    def _dft(self, signal: List[float]) -> List[complex]:
        N: int = len(signal)
        return [sum(signal[n] * cmath.exp(-2j * cmath.pi * k * n / N) for n in range(N)) for k in range(N)]

    def _spectrogram(self, signal: List[float]) -> List[List[float]]:
        step: int = self.window_size - self.overlap
        spectrogram: List[List[float]] = []

        for start in range(0, len(signal) - self.window_size + 1, step):
            windowed_signal: List[float] = signal[start:start + self.window_size]
            dft_result: List[complex] = self._dft(windowed_signal)
            magnitude: List[float] = [abs(freq) for freq in dft_result]
            spectrogram.append(magnitude)

        return spectrogram


    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        if len(signal1) != len(signal2):
            raise ValueError("Both signals must have the same length.")

        spectrogram1: List[List[float]] = self._spectrogram(signal1)
        spectrogram2: List[List[float]] = self._spectrogram(signal2)
        distance: float = Sound._mean_squared_error(spectrogram1, spectrogram2)
        return distance
        
    def example(self):
			
      signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
      signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

      spectrogram_calculator = SpectrogramDistance(window_size=256, overlap=128)

      distance_value: float = spectrogram_calculator.compute(signal1, signal2)

      print("Spectrogram Distance:", distance_value)

import cmath

class CQTDistance(Distance):

    def __init__(self, num_bins: int = 24, window_size: int = 512) -> None:
        super().__init__()
        self.type='sound'

        self.num_bins: int = num_bins
        self.window_size: int = window_size

    def _dft(self, signal: List[float]) -> List[complex]:
        N: int = len(signal)
        return [sum(signal[n] * cmath.exp(-2j * cmath.pi * k * n / N) for n in range(N)) for k in range(N)]

    def _cqt(self, signal: List[float]) -> List[List[float]]:
        step: int = self.window_size
        cqt_matrix: List[List[float]] = []

        for start in range(0, len(signal) - self.window_size + 1, step):
            windowed_signal: List[float] = signal[start:start + self.window_size]
            dft_result: List[complex] = self._dft(windowed_signal)

            # Compute magnitude and split into bins
            magnitude: List[float] = [abs(freq) for freq in dft_result]
            cqt_bins: List[float] = [sum(magnitude[i] for i in range(self.num_bins))]  # Simplified CQT binning
            cqt_matrix.append(cqt_bins)

        return cqt_matrix

    def compute(self, signal1: List[float], signal2: List[float]) -> float:
        if len(signal1) != len(signal2):
            raise ValueError("Both signals must have the same length.")

        cqt1: List[List[float]] = self._cqt(signal1)
        cqt2: List[List[float]] = self._cqt(signal2)

        distance: float = Sound._mean_squared_error(cqt1, cqt2)
        return distance
    def example(self):
      signal1: List[float] = [0.1 * math.sin(2 * math.pi * 440 * t / 16000) for t in range(16000)]
      signal2: List[float] = [0.1 * math.sin(2 * math.pi * 445 * t / 16000) for t in range(16000)]  # Slightly different frequency

      cqt_calculator = CQTDistance(num_bins=24, window_size=512)

      distance_value: float = cqt_calculator.compute(signal1, signal2)

      print("CQT Distance:", distance_value)
      
import wave
from typing import Tuple

class CepstralDistance(Distance):

    def __init__(self, sample_rate: int = 16000, frame_size: int = 512, num_coefficients: int = 13) -> None:
        """
        Initializes the CepstralDistance class with the specified parameters.
        
        :param sample_rate: The sampling rate of the audio signal.
        :param frame_size: The size of each frame used for analysis.
        :param num_coefficients: The number of cepstral coefficients to extract.
        """
        super().__init__()
        self.type='sound'

        self.sample_rate: int = sample_rate
        self.frame_size: int = frame_size
        self.num_coefficients: int = num_coefficients



    def compute_cepstral_coefficients(self, signal: List[float]) -> List[float]:
        """
        Computes the cepstral coefficients of a given audio signal.
        
        :param signal: The input audio signal as a list of floats.
        :return: The cepstral coefficients as a list of floats.
        """
        # Compute the power spectrum (simplified for the example)
        power_spectrum: List[float] = [math.log(abs(s)) for s in signal if s!=0]

        # Apply the inverse Fourier transform to obtain cepstral coefficients
        cepstrum: List[float] = self.inverse_fft(power_spectrum)

        # Return only the first 'num_coefficients' coefficients
        return cepstrum[:self.num_coefficients]



    def compute(self, cepstral_1: List[float], cepstral_2: List[float]) -> float:
        """
        Computes the Euclidean distance between two sets of cepstral coefficients.
        
        :param cepstral_1: The first set of cepstral coefficients.
        :param cepstral_2: The second set of cepstral coefficients.
        :return: The cepstral distance as a float.
        """
        return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(cepstral_1, cepstral_2)))

    def compute_cepstral_distance(self, file1: str, file2: str) -> float:
        """
        Computes the Cepstral Distance between two audio files.
        
        :param file1: Path to the first audio file.
        :param file2: Path to the second audio file.
        :return: The Cepstral Distance as a float.
        """
        audio_data_1, sample_rate_1 = Sound.read_audio(file1)
        audio_data_2, sample_rate_2 = Sound.read_audio(file2)

        if sample_rate_1 != sample_rate_2:
            raise ValueError("Sample rates of the two audio files must be the same.")

        cepstral_1: List[float] = self.compute_cepstral_coefficients(audio_data_1)
        cepstral_2: List[float] = self.compute_cepstral_coefficients(audio_data_2)

        distance: float = self.calculate_distance(cepstral_1, cepstral_2)
        return distance

'''
les fichier ont été générés

if __name__ == "__main__":
    # Generate two different sine wave signals
    duration: float = 2.0  # seconds

    sine_wave1 = generate_sine_wave(frequency=440.0, duration=duration)  # A4 note (440 Hz)
    sine_wave2 = generate_sine_wave(frequency=523.25, duration=duration)  # C5 note (523.25 Hz)

    # Save the generated sine waves to two .wav files
    save_wave("../sample/audio1.wav", sine_wave1)
    save_wave("../sample/audio2.wav", sine_wave2)

    print("Two audio files 'audio1.wav' and 'audio2.wav' have been generated.")
'''
if __name__ == "__main__":
    # Example usage
    file1: str = "../sample/audio1.wav"
    file2: str = "../sample/audio2.wav"

    cepstral_distance_calculator = CepstralDistance()
    distance: float = cepstral_distance_calculator.compute_cepstral_distance(file1, file2)

    print(f"Cepstral Distance: {distance}")

##############################################
#perplexity ai
from typing import List
import math

class SpectralFlatnessMeasure:
    def __init__(self, signal1: List[float], signal2: List[float]):
        """
        Initialize the SpectralFlatnessMeasure class with two sound signals.
        
        :param signal1: First sound signal as a list of float values
        :param signal2: Second sound signal as a list of float values
        """
        self.signal1 = signal1
        self.signal2 = signal2

    def calculate_sfm(self, signal: List[float]) -> float:
        """
        Calculate the Spectral Flatness Measure (SFM) for a given signal.
        
        :param signal: Sound signal as a list of float values
        :return: SFM value as a float
        """
        n = len(signal)
        
        # Calculate the geometric mean
        geometric_mean = math.exp(sum(math.log(abs(x) + 1e-6) for x in signal) / n)
        
        # Calculate the arithmetic mean
        arithmetic_mean = sum(abs(x) for x in signal) / n
        
        # Calculate SFM
        sfm = geometric_mean / arithmetic_mean
        
        return sfm

    def compare_sfm(self) -> float:
        """
        Compare the SFM values of the two signals and return their difference.
        
        :return: Difference between SFM values of signal1 and signal2
        """
        sfm1 = self.calculate_sfm(self.signal1)
        sfm2 = self.calculate_sfm(self.signal2)
        
        return abs(sfm1 - sfm2)
#################################################
'''
from typing import List
import math

class SpectralCentroidDistance:
    def __init__(self, signal1: List[float], signal2: List[float], sample_rate: int = 44100):
        """
        Initialize the SpectralCentroidDistance class with two audio signals.
        
        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param sample_rate: Sampling rate of the audio signals (default: 44100 Hz)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.sample_rate = sample_rate

    def calculate_spectral_centroid(self, signal: List[float]) -> float:
        """
        Calculate the spectral centroid for a given signal.
        
        :param signal: Audio signal as a list of float values
        :return: Spectral centroid value
        """
        magnitudes = self._fft_magnitude(signal)
        frequencies = self._fft_frequencies(len(signal))
        
        weighted_sum = sum(m * f for m, f in zip(magnitudes, frequencies))
        magnitude_sum = sum(magnitudes)
        
        return weighted_sum / magnitude_sum if magnitude_sum != 0 else 0

    def compare_brightness(self) -> float:
        """
        Compare the brightness of the two signals by calculating
        the difference between their spectral centroids.
        
        :return: Absolute difference between spectral centroids
        """
        centroid1 = self.calculate_spectral_centroid(self.signal1)
        centroid2 = self.calculate_spectral_centroid(self.signal2)
        
        return abs(centroid1 - centroid2)

    def _fft_magnitude(self, signal: List[float]) -> List[float]:
        """
        Calculate the magnitude spectrum of the signal using FFT.
        
        :param signal: Input signal
        :return: Magnitude spectrum
        """
        n = len(signal)
        fft = self._fft(signal)
        return [abs(x) for x in fft[:n//2]]

    def _fft_frequencies(self, n: int) -> List[float]:
        """
        Generate the frequency bins for FFT.
        
        :param n: Length of the signal
        :return: List of frequency bins
        """
        return [i * self.sample_rate / n for i in range(n//2)]

    def _fft(self, x: List[float]) -> List[complex]:
        """
        Cooley-Tukey FFT algorithm.
        
        :param x: Input signal
        :return: FFT of the signal
        """
        n = len(x)
        if n <= 1:
            return x
        even = self._fft(x[0::2])
        odd = self._fft(x[1::2])
        twiddle_factors = [math.e ** (-2j * math.pi * k / n) for k in range(n//2)]
        return [even[k] + twiddle_factors[k] * odd[k] for k in range(n//2)] + \
               [even[k] - twiddle_factors[k] * odd[k] for k in range(n//2)]
'''
##########################################
from typing import List
import math

class SpectralFlux:
    def __init__(self, signal1: List[float], signal2: List[float], frame_size: int = 1024, hop_size: int = 512):
        """
        Initialize the SpectralFlux class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param frame_size: Size of each frame for spectral analysis (default: 1024)
        :param hop_size: Number of samples between successive frames (default: 512)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.frame_size = frame_size
        self.hop_size = hop_size

    def calculate_spectral_flux(self, signal: List[float]) -> List[float]:
        """
        Calculate the Spectral Flux for a given signal.

        :param signal: Audio signal as a list of float values
        :return: List of Spectral Flux values for each frame
        """
        frames = self._frame_signal(signal)
        spectra = [self._calculate_spectrum(frame) for frame in frames]
        
        flux = []
        for i in range(1, len(spectra)):
            diff = sum((spectra[i][j] - spectra[i-1][j])**2 for j in range(len(spectra[i])))
            flux.append(math.sqrt(diff))
        
        return flux

    def compare_spectral_flux(self) -> float:
        """
        Compare the Spectral Flux between the two signals.

        :return: Mean absolute difference of Spectral Flux values
        """
        flux1 = self.calculate_spectral_flux(self.signal1)
        flux2 = self.calculate_spectral_flux(self.signal2)
        
        # Ensure both flux lists have the same length
        min_length = min(len(flux1), len(flux2))
        flux1 = flux1[:min_length]
        flux2 = flux2[:min_length]
        
        # Calculate mean absolute difference
        diff = sum(abs(f1 - f2) for f1, f2 in zip(flux1, flux2)) / min_length
        return diff

    def _frame_signal(self, signal: List[float]) -> List[List[float]]:
        """
        Divide the signal into overlapping frames.

        :param signal: Input signal
        :return: List of frames
        """
        frames = []
        for i in range(0, len(signal) - self.frame_size + 1, self.hop_size):
            frames.append(signal[i:i+self.frame_size])
        return frames

    def _calculate_spectrum(self, frame: List[float]) -> List[float]:
        """
        Calculate the magnitude spectrum of a frame using FFT.

        :param frame: Input frame
        :return: Magnitude spectrum
        """
        fft_result = self._fft(frame)
        return [abs(x) for x in fft_result[:len(frame)//2]]

    def _fft(self, x: List[float]) -> List[complex]:
        """
        Cooley-Tukey FFT algorithm.

        :param x: Input signal
        :return: FFT of the signal
        """
        n = len(x)
        if n <= 1:
            return x
        even = self._fft(x[0::2])
        odd = self._fft(x[1::2])
        twiddle_factors = [math.e ** (-2j * math.pi * k / n) for k in range(n//2)]
        return [even[k] + twiddle_factors[k] * odd[k] for k in range(n//2)] + \
               [even[k] - twiddle_factors[k] * odd[k] for k in range(n//2)]

from typing import List
import math

class EnvelopeCrossDistance:
    def __init__(self, signal1: List[float], signal2: List[float], frame_size: int = 1024, hop_length: int = 512):
        """
        Initialize the EnvelopeCrossDistance class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param frame_size: Size of each frame for envelope calculation (default: 1024)
        :param hop_length: Number of samples between successive frames (default: 512)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.frame_size = frame_size
        self.hop_length = hop_length

    def calculate_envelope(self, signal: List[float]) -> List[float]:
        """
        Calculate the amplitude envelope for a given signal.

        :param signal: Audio signal as a list of float values
        :return: List of amplitude envelope values
        """
        envelope = []
        for i in range(0, len(signal), self.hop_length):
            frame = signal[i:i + self.frame_size]
            envelope.append(max(abs(x) for x in frame))
        return envelope

    def calculate_cross_distance(self) -> float:
        """
        Calculate the Envelope Cross-Distance between the two signals.

        :return: Envelope Cross-Distance value
        """
        envelope1 = self.calculate_envelope(self.signal1)
        envelope2 = self.calculate_envelope(self.signal2)

        # Ensure both envelopes have the same length
        min_length = min(len(envelope1), len(envelope2))
        envelope1 = envelope1[:min_length]
        envelope2 = envelope2[:min_length]

        # Calculate the Euclidean distance between envelopes
        distance = math.sqrt(sum((e1 - e2) ** 2 for e1, e2 in zip(envelope1, envelope2)))
        
        # Normalize by the number of frames
        normalized_distance = distance / min_length

        return normalized_distance

##################################################
from typing import List
import math

class ShortTimeEnergyDistance:
    def __init__(self, signal1: List[float], signal2: List[float], frame_size: int = 1024, hop_size: int = 512):
        """
        Initialize the ShortTimeEnergyDistance class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param frame_size: Size of each frame for energy calculation (default: 1024)
        :param hop_size: Number of samples between successive frames (default: 512)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.frame_size = frame_size
        self.hop_size = hop_size

    def calculate_short_time_energy(self, signal: List[float]) -> List[float]:
        """
        Calculate the Short-Time Energy for a given signal.

        :param signal: Audio signal as a list of float values
        :return: List of Short-Time Energy values
        """
        energy = []
        for i in range(0, len(signal) - self.frame_size + 1, self.hop_size):
            frame = signal[i:i + self.frame_size]
            frame_energy = sum(x**2 for x in frame) / self.frame_size
            energy.append(frame_energy)
        return energy

    def calculate_distance(self) -> float:
        """
        Calculate the Short-Time Energy Distance between the two signals.

        :return: Short-Time Energy Distance value
        """
        energy1 = self.calculate_short_time_energy(self.signal1)
        energy2 = self.calculate_short_time_energy(self.signal2)

        min_length = min(len(energy1), len(energy2))
        energy1 = energy1[:min_length]
        energy2 = energy2[:min_length]

        distance = math.sqrt(sum((e1 - e2)**2 for e1, e2 in zip(energy1, energy2)))
        normalized_distance = distance / min_length

        return normalized_distance

####################################
from typing import List
import math

class FrequencyBinDistance:
    def __init__(self, signal1: List[float], signal2: List[float], sample_rate: int = 44100, fft_size: int = 2048):
        """
        Initialize the FrequencyBinDistance class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param sample_rate: Sampling rate of the audio signals (default: 44100 Hz)
        :param fft_size: Size of the FFT (default: 2048)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.sample_rate = sample_rate
        self.fft_size = fft_size
        self.frequency_bin_count = fft_size // 2

    def calculate_spectrum(self, signal: List[float]) -> List[float]:
        """
        Calculate the magnitude spectrum for a given signal.

        :param signal: Audio signal as a list of float values
        :return: Magnitude spectrum
        """
        fft_result = self._fft(signal[:self.fft_size])
        return [abs(x) for x in fft_result[:self.frequency_bin_count]]

    def calculate_bin_distance(self, start_freq: float, end_freq: float) -> float:
        """
        Calculate the Frequency Bin Distance between the two signals for a specific frequency range.

        :param start_freq: Start frequency of the range to compare (in Hz)
        :param end_freq: End frequency of the range to compare (in Hz)
        :return: Frequency Bin Distance value
        """
        spectrum1 = self.calculate_spectrum(self.signal1)
        spectrum2 = self.calculate_spectrum(self.signal2)

        bin_width = self.sample_rate / self.fft_size
        start_bin = int(start_freq / bin_width)
        end_bin = min(int(end_freq / bin_width), self.frequency_bin_count)

        distance = math.sqrt(sum((spectrum1[i] - spectrum2[i])**2 for i in range(start_bin, end_bin)))
        normalized_distance = distance / (end_bin - start_bin)

        return normalized_distance

    def _fft(self, x: List[float]) -> List[complex]:
        """
        Cooley-Tukey FFT algorithm.

        :param x: Input signal
        :return: FFT of the signal
        """
        n = len(x)
        if n <= 1:
            return x
        even = self._fft(x[0::2])
        odd = self._fft(x[1::2])
        twiddle_factors = [math.e ** (-2j * math.pi * k / n) for k in range(n//2)]
        return [even[k] + twiddle_factors[k] * odd[k] for k in range(n//2)] + \
               [even[k] - twiddle_factors[k] * odd[k] for k in range(n//2)]

#################################################
from typing import List
import math

class PitchDistance:
    def __init__(self, signal1: List[float], signal2: List[float], sample_rate: int = 44100, frame_size: int = 2048, num_harmonics: int = 5):
        """
        Initialize the PitchDistance class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param sample_rate: Sampling rate of the audio signals (default: 44100 Hz)
        :param frame_size: Size of the frame for FFT (default: 2048)
        :param num_harmonics: Number of harmonics to consider in HPS (default: 5)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.num_harmonics = num_harmonics

    def calculate_pitch_distance(self) -> float:
        """
        Calculate the pitch distance between the two signals using HPS.

        :return: Pitch distance in Hz
        """
        pitch1 = self._estimate_pitch(self.signal1)
        pitch2 = self._estimate_pitch(self.signal2)
        return abs(pitch1 - pitch2)

    def _estimate_pitch(self, signal: List[float]) -> float:
        """
        Estimate the pitch of a signal using Harmonic Product Spectrum.

        :param signal: Audio signal as a list of float values
        :return: Estimated pitch in Hz
        """
        spectrum = self._calculate_spectrum(signal)
        hps = self._harmonic_product_spectrum(spectrum)
        peak_index = max(range(len(hps)), key=hps.__getitem__)
        return peak_index * self.sample_rate / self.frame_size

    def _calculate_spectrum(self, signal: List[float]) -> List[float]:
        """
        Calculate the magnitude spectrum of the signal.

        :param signal: Audio signal as a list of float values
        :return: Magnitude spectrum
        """
        fft_result = self._fft(signal[:self.frame_size])
        return [abs(x) for x in fft_result[:self.frame_size//2]]

    def _harmonic_product_spectrum(self, spectrum: List[float]) -> List[float]:
        """
        Apply Harmonic Product Spectrum algorithm.

        :param spectrum: Magnitude spectrum of the signal
        :return: HPS result
        """
        hps = spectrum.copy()
        for harmonic in range(2, self.num_harmonics + 1):
            downsampled = [0] * (len(spectrum) // harmonic)
            for i in range(len(downsampled)):
                downsampled[i] = spectrum[i * harmonic]
            hps = [hps[i] * downsampled[i] for i in range(len(downsampled))]
        return hps

    def _fft(self, x: List[float]) -> List[complex]:
        """
        Cooley-Tukey FFT algorithm.

        :param x: Input signal
        :return: FFT of the signal
        """
        n = len(x)
        if n <= 1:
            return x
        even = self._fft(x[0::2])
        odd = self._fft(x[1::2])
        twiddle_factors = [math.e ** (-2j * math.pi * k / n) for k in range(n//2)]
        return [even[k] + twiddle_factors[k] * odd[k] for k in range(n//2)] + \
               [even[k] - twiddle_factors[k] * odd[k] for k in range(n//2)]

#################################
from typing import List
import math

class LogFrequencySpectralDistance:
    def __init__(self, signal1: List[float], signal2: List[float], sample_rate: int = 44100, frame_size: int = 2048, min_freq: float = 20, max_freq: float = 20000, num_bins: int = 128):
        """
        Initialize the LogFrequencySpectralDistance class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param sample_rate: Sampling rate of the audio signals (default: 44100 Hz)
        :param frame_size: Size of the frame for FFT (default: 2048)
        :param min_freq: Minimum frequency for log-scale bins (default: 20 Hz)
        :param max_freq: Maximum frequency for log-scale bins (default: 20000 Hz)
        :param num_bins: Number of logarithmically spaced frequency bins (default: 128)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.num_bins = num_bins
        self.log_freq_bins = self._create_log_freq_bins()

    def calculate_distance(self) -> float:
        """
        Calculate the Log-Frequency Spectral Distance between the two signals.

        :return: Log-Frequency Spectral Distance value
        """
        spectrum1 = self._calculate_log_spectrum(self.signal1)
        spectrum2 = self._calculate_log_spectrum(self.signal2)

        # Calculate Euclidean distance between log spectra
        distance = math.sqrt(sum((s1 - s2) ** 2 for s1, s2 in zip(spectrum1, spectrum2)))
        return distance

    def _calculate_log_spectrum(self, signal: List[float]) -> List[float]:
        """
        Calculate the log-frequency spectrum for a given signal.

        :param signal: Audio signal as a list of float values
        :return: Log-frequency spectrum
        """
        linear_spectrum = self._calculate_spectrum(signal)
        log_spectrum = [0] * self.num_bins

        for i, (low, high) in enumerate(self.log_freq_bins):
            bin_energy = sum(linear_spectrum[j] for j in range(low, high))
            log_spectrum[i] = math.log(bin_energy + 1e-10)  # Add small value to avoid log(0)

        return log_spectrum

    def _calculate_spectrum(self, signal: List[float]) -> List[float]:
        """
        Calculate the magnitude spectrum of the signal.

        :param signal: Audio signal as a list of float values
        :return: Magnitude spectrum
        """
        fft_result = self._fft(signal[:self.frame_size])
        return [abs(x) for x in fft_result[:self.frame_size//2]]

    def _create_log_freq_bins(self) -> List[tuple]:
        """
        Create logarithmically spaced frequency bins.

        :return: List of tuples representing frequency bin ranges
        """
        min_log = math.log(self.min_freq)
        max_log = math.log(self.max_freq)
        log_freq_step = (max_log - min_log) / self.num_bins

        bins = []
        for i in range(self.num_bins):
            low_freq = math.exp(min_log + i * log_freq_step)
            high_freq = math.exp(min_log + (i + 1) * log_freq_step)
            low_bin = int(low_freq * self.frame_size / self.sample_rate)
            high_bin = int(high_freq * self.frame_size / self.sample_rate)
            bins.append((low_bin, high_bin))

        return bins

    def _fft(self, x: List[float]) -> List[complex]:
        """
        Cooley-Tukey FFT algorithm.

        :param x: Input signal
        :return: FFT of the signal
        """
        n = len(x)
        if n <= 1:
            return x
        even = self._fft(x[0::2])
        odd = self._fft(x[1::2])
        twiddle_factors = [math.e ** (-2j * math.pi * k / n) for k in range(n//2)]
        return [even[k] + twiddle_factors[k] * odd[k] for k in range(n//2)] + \
               [even[k] - twiddle_factors[k] * odd[k] for k in range(n//2)]

#########################################
from typing import List, Tuple
import math

class CQTDistance:
    def __init__(self, signal1: List[float], signal2: List[float], sample_rate: int = 44100, 
                 min_freq: float = 55.0, max_freq: float = 7040.0, bins_per_octave: int = 12):
        """
        Initialize the CQTDistance class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param sample_rate: Sampling rate of the audio signals (default: 44100 Hz)
        :param min_freq: Minimum frequency for CQT (default: 55.0 Hz, A1 note)
        :param max_freq: Maximum frequency for CQT (default: 7040.0 Hz, A8 note)
        :param bins_per_octave: Number of bins per octave (default: 12, semitones)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.sample_rate = sample_rate
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.bins_per_octave = bins_per_octave
        self.num_octaves = math.ceil(math.log2(max_freq / min_freq))
        self.total_bins = self.num_octaves * bins_per_octave
        self.q_factor = 1 / (2 ** (1 / bins_per_octave) - 1)
        self.kernels = self._create_cqt_kernels()

    def calculate_distance(self) -> float:
        """
        Calculate the CQT distance between the two signals.

        :return: CQT distance value
        """
        cqt1 = self._compute_cqt(self.signal1)
        cqt2 = self._compute_cqt(self.signal2)

        # Calculate Euclidean distance between CQT representations
        distance = math.sqrt(sum((abs(c1) - abs(c2)) ** 2 for c1, c2 in zip(cqt1, cqt2)))
        return distance

    def _compute_cqt(self, signal: List[float]) -> List[complex]:
        """
        Compute the Constant-Q Transform for a given signal.

        :param signal: Audio signal as a list of float values
        :return: CQT coefficients
        """
        cqt = []
        for kernel in self.kernels:
            coefficient = sum(s * k.conjugate() for s, k in zip(signal, kernel))
            cqt.append(coefficient)
        return cqt

    def _create_cqt_kernels(self) -> List[List[complex]]:
        """
        Create CQT kernels for each frequency bin.

        :return: List of CQT kernels
        """
        kernels = []
        for k in range(self.total_bins):
            freq = self.min_freq * (2 ** (k / self.bins_per_octave))
            kernel_length = int(self.q_factor * self.sample_rate / freq)
            kernel = self._create_kernel(freq, kernel_length)
            kernels.append(kernel)
        return kernels

    def _create_kernel(self, freq: float, length: int) -> List[complex]:
        """
        Create a single CQT kernel for a specific frequency.

        :param freq: Frequency for the kernel
        :param length: Length of the kernel
        :return: CQT kernel as a list of complex values
        """
        kernel = []
        for n in range(length):
            t = n / self.sample_rate
            real = math.cos(2 * math.pi * freq * t)
            imag = math.sin(2 * math.pi * freq * t)
            window = 0.5 * (1 - math.cos(2 * math.pi * n / (length - 1)))  # Hann window
            kernel.append(complex(real * window, -imag * window))
        return kernel

#########################################
from typing import List
import math

class PEAQ:
    def __init__(self, reference: List[float], test: List[float], sample_rate: int = 44100):
        """
        Initialize the PEAQ class with reference and test audio signals.

        :param reference: Reference audio signal as a list of float values
        :param test: Test audio signal as a list of float values
        :param sample_rate: Sampling rate of the audio signals (default: 44100 Hz)
        """
        self.reference = reference
        self.test = test
        self.sample_rate = sample_rate
        self.frame_size = 2048
        self.hop_size = 1024

    def calculate_odg(self) -> float:
        """
        Calculate the Objective Difference Grade (ODG) between reference and test signals.

        :return: ODG value ranging from -4 (very annoying) to 0 (imperceptible difference)
        """
        movs = self._calculate_movs()
        odg = self._map_movs_to_odg(movs)
        return odg

    def _calculate_movs(self) -> List[float]:
        """
        Calculate Model Output Variables (MOVs) for PEAQ.

        :return: List of MOV values
        """
        ref_frames = self._frame_signal(self.reference)
        test_frames = self._frame_signal(self.test)
        
        total_noise_to_mask_ratio = 0
        total_bandwidth_difference = 0
        
        for ref_frame, test_frame in zip(ref_frames, test_frames):
            ref_spectrum = self._fft(ref_frame)
            test_spectrum = self._fft(test_frame)
            
            noise_to_mask_ratio = self._calculate_noise_to_mask_ratio(ref_spectrum, test_spectrum)
            bandwidth_difference = self._calculate_bandwidth_difference(ref_spectrum, test_spectrum)
            
            total_noise_to_mask_ratio += noise_to_mask_ratio
            total_bandwidth_difference += bandwidth_difference
        
        avg_noise_to_mask_ratio = total_noise_to_mask_ratio / len(ref_frames)
        avg_bandwidth_difference = total_bandwidth_difference / len(ref_frames)
        
        return [avg_noise_to_mask_ratio, avg_bandwidth_difference]

    def _map_movs_to_odg(self, movs: List[float]) -> float:
        """
        Map Model Output Variables (MOVs) to Objective Difference Grade (ODG).

        :param movs: List of MOV values
        :return: ODG value
        """
        # This is a simplified mapping function and doesn't represent the actual PEAQ neural network
        odg = -4 * (movs[0] / 30) - (movs[1] / 5)
        return max(-4, min(0, odg))

    def _frame_signal(self, signal: List[float]) -> List[List[float]]:
        """
        Divide the signal into overlapping frames.

        :param signal: Input signal
        :return: List of frames
        """
        frames = []
        for i in range(0, len(signal) - self.frame_size, self.hop_size):
            frames.append(signal[i:i+self.frame_size])
        return frames

    def _fft(self, frame: List[float]) -> List[complex]:
        """
        Perform Fast Fourier Transform on a frame.

        :param frame: Input frame
        :return: FFT result
        """
        n = len(frame)
        if n <= 1:
            return frame
        even = self._fft(frame[0::2])
        odd = self._fft(frame[1::2])
        return [even[k] + math.e**(-2j*math.pi*k/n) * odd[k] for k in range(n//2)] + \
               [even[k] - math.e**(-2j*math.pi*k/n) * odd[k] for k in range(n//2)]

    def _calculate_noise_to_mask_ratio(self, ref_spectrum: List[complex], test_spectrum: List[complex]) -> float:
        """
        Calculate the Noise-to-Mask Ratio (NMR) between reference and test spectra.

        :param ref_spectrum: Reference spectrum
        :param test_spectrum: Test spectrum
        :return: NMR value
        """
        # Simplified NMR calculation
        ref_power = sum(abs(x)**2 for x in ref_spectrum)
        noise_power = sum(abs(x-y)**2 for x, y in zip(ref_spectrum, test_spectrum))
        return 10 * math.log10(noise_power / (ref_power + 1e-10))

    def _calculate_bandwidth_difference(self, ref_spectrum: List[complex], test_spectrum: List[complex]) -> float:
        """
        Calculate the bandwidth difference between reference and test spectra.

        :param ref_spectrum: Reference spectrum
        :param test_spectrum: Test spectrum
        :return: Bandwidth difference value
        """
        # Simplified bandwidth difference calculation
        ref_bandwidth = self._estimate_bandwidth(ref_spectrum)
        test_bandwidth = self._estimate_bandwidth(test_spectrum)
        return abs(ref_bandwidth - test_bandwidth)

    def _estimate_bandwidth(self, spectrum: List[complex]) -> float:
        """
        Estimate the bandwidth of a spectrum.

        :param spectrum: Input spectrum
        :return: Estimated bandwidth
        """
        threshold = max(abs(x) for x in spectrum) / 100
        for i in range(len(spectrum) - 1, 0, -1):
            if abs(spectrum[i]) > threshold:
                return i * self.sample_rate / len(spectrum)
        return 0

##################################
from typing import List
import math

class PerceptualSpectralDivergence:
    def __init__(self, signal1: List[float], signal2: List[float], sample_rate: int = 44100, frame_size: int = 2048, hop_size: int = 512):
        """
        Initialize the PerceptualSpectralDivergence class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param sample_rate: Sampling rate of the audio signals (default: 44100 Hz)
        :param frame_size: Size of each frame for spectral analysis (default: 2048)
        :param hop_size: Number of samples between successive frames (default: 512)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.hop_size = hop_size
        self.mel_filters = self._create_mel_filterbank(num_filters=40, low_freq=0, high_freq=sample_rate/2)

    def calculate_divergence(self) -> float:
        """
        Calculate the Perceptual Spectral Divergence between the two signals.

        :return: Perceptual Spectral Divergence value
        """
        frames1 = self._frame_signal(self.signal1)
        frames2 = self._frame_signal(self.signal2)

        divergence = 0.0
        for frame1, frame2 in zip(frames1, frames2):
            spectrum1 = self._calculate_power_spectrum(frame1)
            spectrum2 = self._calculate_power_spectrum(frame2)
            
            mel_spectrum1 = self._apply_mel_filterbank(spectrum1)
            mel_spectrum2 = self._apply_mel_filterbank(spectrum2)
            
            frame_divergence = self._kullback_leibler_divergence(mel_spectrum1, mel_spectrum2)
            divergence += frame_divergence

        return divergence / len(frames1)

    def _frame_signal(self, signal: List[float]) -> List[List[float]]:
        """
        Divide the signal into overlapping frames.

        :param signal: Input signal
        :return: List of frames
        """
        frames = []
        for i in range(0, len(signal) - self.frame_size + 1, self.hop_size):
            frames.append(signal[i:i+self.frame_size])
        return frames

    def _calculate_power_spectrum(self, frame: List[float]) -> List[float]:
        """
        Calculate the power spectrum of a frame.

        :param frame: Input frame
        :return: Power spectrum
        """
        fft_result = self._fft(frame)
        return [abs(x)**2 for x in fft_result[:len(frame)//2]]

    def _fft(self, x: List[float]) -> List[complex]:
        """
        Cooley-Tukey FFT algorithm.

        :param x: Input signal
        :return: FFT of the signal
        """
        n = len(x)
        if n <= 1:
            return x
        even = self._fft(x[0::2])
        odd = self._fft(x[1::2])
        twiddle_factors = [math.e ** (-2j * math.pi * k / n) for k in range(n//2)]
        return [even[k] + twiddle_factors[k] * odd[k] for k in range(n//2)] + \
               [even[k] - twiddle_factors[k] * odd[k] for k in range(n//2)]

    def _create_mel_filterbank(self, num_filters: int, low_freq: float, high_freq: float) -> List[List[float]]:
        """
        Create a Mel filterbank.

        :param num_filters: Number of Mel filters
        :param low_freq: Lowest frequency to consider
        :param high_freq: Highest frequency to consider
        :return: Mel filterbank
        """
        mel_low = self._hz_to_mel(low_freq)
        mel_high = self._hz_to_mel(high_freq)
        mel_points = [mel_low + i * (mel_high - mel_low) / (num_filters + 1) for i in range(num_filters + 2)]
        hz_points = [self._mel_to_hz(mel) for mel in mel_points]
        bin_indices = [int(round(hz * (self.frame_size / self.sample_rate))) for hz in hz_points]

        filters = [[0.0] * (self.frame_size // 2) for _ in range(num_filters)]
        for i in range(num_filters):
            for j in range(bin_indices[i], bin_indices[i+1]):
                filters[i][j] = (j - bin_indices[i]) / (bin_indices[i+1] - bin_indices[i])
            for j in range(bin_indices[i+1], bin_indices[i+2]):
                filters[i][j] = (bin_indices[i+2] - j) / (bin_indices[i+2] - bin_indices[i+1])
        return filters

    def _apply_mel_filterbank(self, spectrum: List[float]) -> List[float]:
        """
        Apply Mel filterbank to the power spectrum.

        :param spectrum: Power spectrum
        :return: Mel-filtered spectrum
        """
        return [sum(f * s for f, s in zip(filter_bank, spectrum)) for filter_bank in self.mel_filters]

    def _kullback_leibler_divergence(self, p: List[float], q: List[float]) -> float:
        """
        Calculate the Kullback-Leibler divergence between two distributions.

        :param p: First distribution
        :param q: Second distribution
        :return: KL divergence
        """
        return sum(p[i] * math.log(p[i] / q[i]) for i in range(len(p)) if p[i] > 0 and q[i] > 0)

    def _hz_to_mel(self, hz: float) -> float:
        """
        Convert Hz to Mel scale.

        :param hz: Frequency in Hz
        :return: Frequency in Mel scale
        """
        return 2595 * math.log10(1 + hz / 700)

    def _mel_to_hz(self, mel: float) -> float:
        """
        Convert Mel scale to Hz.

        :param mel: Frequency in Mel scale
        :return: Frequency in Hz
        """
        return 700 * (10**(mel / 2595) - 1)

#################################################
from typing import List, Tuple
import math

class PsychoacousticDistance:
    def __init__(self, signal1: List[float], signal2: List[float], sample_rate: int = 44100, frame_size: int = 2048, hop_size: int = 512):
        """
        Initialize the PsychoacousticDistance class with two audio signals.

        :param signal1: First audio signal as a list of float values
        :param signal2: Second audio signal as a list of float values
        :param sample_rate: Sampling rate of the audio signals (default: 44100 Hz)
        :param frame_size: Size of each frame for spectral analysis (default: 2048)
        :param hop_size: Number of samples between successive frames (default: 512)
        """
        self.signal1 = signal1
        self.signal2 = signal2
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.hop_size = hop_size
        self.bark_scale = self._create_bark_scale()

    def calculate_distance(self) -> float:
        """
        Calculate the Psychoacoustic Distance between the two signals.

        :return: Psychoacoustic Distance value
        """
        frames1 = self._frame_signal(self.signal1)
        frames2 = self._frame_signal(self.signal2)

        total_distance = 0.0
        for frame1, frame2 in zip(frames1, frames2):
            spectrum1 = self._calculate_power_spectrum(frame1)
            spectrum2 = self._calculate_power_spectrum(frame2)
            
            bark_spectrum1 = self._to_bark_scale(spectrum1)
            bark_spectrum2 = self._to_bark_scale(spectrum2)
            
            masked_diff = self._apply_masking(bark_spectrum1, bark_spectrum2)
            frame_distance = sum(masked_diff)
            total_distance += frame_distance

        return total_distance / len(frames1)

    def _frame_signal(self, signal: List[float]) -> List[List[float]]:
        """
        Divide the signal into overlapping frames.

        :param signal: Input signal
        :return: List of frames
        """
        frames = []
        for i in range(0, len(signal) - self.frame_size + 1, self.hop_size):
            frames.append(signal[i:i+self.frame_size])
        return frames

    def _calculate_power_spectrum(self, frame: List[float]) -> List[float]:
        """
        Calculate the power spectrum of a frame.

        :param frame: Input frame
        :return: Power spectrum
        """
        fft_result = self._fft(frame)
        return [abs(x)**2 for x in fft_result[:len(frame)//2]]

    def _fft(self, x: List[float]) -> List[complex]:
        """
        Cooley-Tukey FFT algorithm.

        :param x: Input signal
        :return: FFT of the signal
        """
        n = len(x)
        if n <= 1:
            return x
        even = self._fft(x[0::2])
        odd = self._fft(x[1::2])
        twiddle_factors = [math.e ** (-2j * math.pi * k / n) for k in range(n//2)]
        return [even[k] + twiddle_factors[k] * odd[k] for k in range(n//2)] + \
               [even[k] - twiddle_factors[k] * odd[k] for k in range(n//2)]

    def _create_bark_scale(self) -> List[Tuple[float, float]]:
        """
        Create Bark scale frequency bands.

        :return: List of tuples representing Bark bands (lower_freq, upper_freq)
        """
        bark_bands = []
        for bark in range(25):  # 25 Bark bands
            lower_freq = 600 * math.sinh(bark / 6)
            upper_freq = 600 * math.sinh((bark + 1) / 6)
            bark_bands.append((lower_freq, upper_freq))
        return bark_bands

    def _to_bark_scale(self, spectrum: List[float]) -> List[float]:
        """
        Convert linear frequency spectrum to Bark scale.

        :param spectrum: Power spectrum
        :return: Bark scale spectrum
        """
        bark_spectrum = [0.0] * len(self.bark_scale)
        for i, (lower, upper) in enumerate(self.bark_scale):
            lower_bin = int(lower * self.frame_size / self.sample_rate)
            upper_bin = int(upper * self.frame_size / self.sample_rate)
            bark_spectrum[i] = sum(spectrum[lower_bin:upper_bin])
        return bark_spectrum

    def _apply_masking(self, spectrum1: List[float], spectrum2: List[float]) -> List[float]:
        """
        Apply a simple masking model to the difference between two spectra.

        :param spectrum1: First Bark scale spectrum
        :param spectrum2: Second Bark scale spectrum
        :return: Masked difference between spectra
        """
        masked_diff = []
        for i in range(len(spectrum1)):
            diff = abs(spectrum1[i] - spectrum2[i])
            mask_threshold = max(spectrum1[i], spectrum2[i]) * 0.1  # Simplified masking threshold
            masked_diff.append(max(0, diff - mask_threshold))
        return masked_diff

####################################
from typing import List, Tuple
import math

class MelFrequencyPerceptualDistance:
    def __init__(self, sample_rate: int, frame_size: int, hop_length: int):
        """
        Initialize the MelFrequencyPerceptualDistance calculator.

        Args:
            sample_rate (int): The sample rate of the audio.
            frame_size (int): The size of each frame for STFT.
            hop_length (int): The number of samples between successive frames.
        """
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.hop_length = hop_length

    def mel_scale(self, frequency: float) -> float:
        """
        Convert frequency to mel scale.

        Args:
            frequency (float): The frequency in Hz.

        Returns:
            float: The mel scale value.
        """
        return 2595 * math.log10(1 + frequency / 700)

    def stft(self, signal: List[float]) -> List[List[complex]]:
        """
        Perform Short-Time Fourier Transform (STFT) on the signal.

        Args:
            signal (List[float]): The input audio signal.

        Returns:
            List[List[complex]]: The STFT of the signal.
        """
        stft_result = []
        for i in range(0, len(signal) - self.frame_size, self.hop_length):
            frame = signal[i:i+self.frame_size]
            windowed_frame = [x * 0.54 - 0.46 * math.cos((2 * math.pi * n) / (self.frame_size - 1)) 
                              for n, x in enumerate(frame)]  # Hamming window
            fft_frame = self._fft(windowed_frame)
            stft_result.append(fft_frame)
        return stft_result

    def _fft(self, frame: List[float]) -> List[complex]:
        """
        Perform Fast Fourier Transform (FFT) on a frame.

        Args:
            frame (List[float]): The input frame.

        Returns:
            List[complex]: The FFT of the frame.
        """
        n = len(frame)
        if n <= 1:
            return frame
        even = self._fft(frame[0::2])
        odd = self._fft(frame[1::2])
        combined = [0] * n
        for k in range(n//2):
            t = math.e ** (-2j * math.pi * k / n) * odd[k]
            combined[k] = even[k] + t
            combined[k + n//2] = even[k] - t
        return combined

    def mel_spectrogram(self, stft_result: List[List[complex]]) -> List[List[float]]:
        """
        Convert STFT to mel spectrogram.

        Args:
            stft_result (List[List[complex]]): The STFT of the signal.

        Returns:
            List[List[float]]: The mel spectrogram.
        """
        num_mel_filters = 128
        mel_filters = self._create_mel_filterbank(num_mel_filters)
        
        mel_spec = []
        for frame in stft_result:
            power_spectrum = [abs(x)**2 for x in frame]
            mel_frame = [sum(f * p for f, p in zip(filter_bank, power_spectrum)) 
                         for filter_bank in mel_filters]
            mel_spec.append(mel_frame)
        return mel_spec

    def _create_mel_filterbank(self, num_filters: int) -> List[List[float]]:
        """
        Create a mel filterbank.

        Args:
            num_filters (int): The number of mel filters to create.

        Returns:
            List[List[float]]: The mel filterbank.
        """
        min_freq = 0
        max_freq = self.sample_rate / 2
        min_mel = self.mel_scale(min_freq)
        max_mel = self.mel_scale(max_freq)
        mel_points = [min_mel + i * (max_mel - min_mel) / (num_filters + 1) for i in range(num_filters + 2)]
        hz_points = [700 * (10**(m / 2595) - 1) for m in mel_points]
        
        fft_bins = [int((self.frame_size + 1) * h / self.sample_rate) for h in hz_points]
        
        filters = [[0] * (self.frame_size // 2 + 1) for _ in range(num_filters)]
        for i in range(num_filters):
            for j in range(fft_bins[i], fft_bins[i+1]):
                filters[i][j] = (j - fft_bins[i]) / (fft_bins[i+1] - fft_bins[i])
            for j in range(fft_bins[i+1], fft_bins[i+2]):
                filters[i][j] = (fft_bins[i+2] - j) / (fft_bins[i+2] - fft_bins[i+1])
        return filters

    def calculate_distance(self, sound1: List[float], sound2: List[float]) -> float:
        """
        Calculate the Mel-Frequency Perceptual Distance between two sounds.

        Args:
            sound1 (List[float]): The first sound signal.
            sound2 (List[float]): The second sound signal.

        Returns:
            float: The perceptual distance between the two sounds.
        """
        stft1 = self.stft(sound1)
        stft2 = self.stft(sound2)
        
        mel_spec1 = self.mel_spectrogram(stft1)
        mel_spec2 = self.mel_spectrogram(stft2)
        
        distance = 0
        for frame1, frame2 in zip(mel_spec1, mel_spec2):
            for bin1, bin2 in zip(frame1, frame2):
                distance += (bin1 - bin2) ** 2
        
        return math.sqrt(distance)
###########################################
import numpy as np
import librosa
from typing import List

class PLPDistance:
    def __init__(self, sample_rate: int, frame_size: int, hop_length: int, n_mels: int, n_plp: int):
        """
        Initialize the PLPDistance calculator.

        Args:
            sample_rate (int): The sample rate of the audio.
            frame_size (int): The size of each frame for analysis.
            hop_length (int): Number of samples between successive frames.
            n_mels (int): Number of Mel bands to generate.
            n_plp (int): Number of PLP coefficients to compute.
        """
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.hop_length = hop_length
        self.n_mels = n_mels
        self.n_plp = n_plp

    def _compute_plp(self, signal: np.ndarray) -> np.ndarray:
        """
        Compute PLP coefficients for a given signal.

        Args:
            signal (np.ndarray): The input audio signal.

        Returns:
            np.ndarray: The PLP coefficients.
        """
        # Compute mel spectrogram
        mel_spec = librosa.feature.melspectrogram(
            y=signal,
            sr=self.sample_rate,
            n_fft=self.frame_size,
            hop_length=self.hop_length,
            n_mels=self.n_mels
        )

        # Convert to dB scale
        mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

        # Apply equal-loudness filter
        equal_loudness = librosa.core.A_weighting(librosa.mel_frequencies(n_mels=self.n_mels, fmax=self.sample_rate/2))
        mel_spec_eq = mel_spec_db + equal_loudness[:, np.newaxis]

        # Intensity-loudness power law
        mel_spec_pow = np.power(10.0, mel_spec_eq / 10.0)
        mel_spec_pow = np.power(mel_spec_pow, 0.33)

        # Compute PLP coefficients
        plp = librosa.feature.mfcc(
            S=librosa.power_to_db(mel_spec_pow),
            n_mfcc=self.n_plp,
            dct_type=2,
            norm='ortho'
        )

        return plp

    def calculate_distance(self, sound1: List[float], sound2: List[float]) -> float:
        """
        Calculate the distance between two sounds using PLP coefficients.

        Args:
            sound1 (List[float]): The first sound signal.
            sound2 (List[float]): The second sound signal.

        Returns:
            float: The distance between the two sounds based on PLP coefficients.
        """
        # Convert lists to numpy arrays
        signal1 = np.array(sound1)
        signal2 = np.array(sound2)

        # Compute PLP coefficients
        plp1 = self._compute_plp(signal1)
        plp2 = self._compute_plp(signal2)

        # Ensure the PLPs have the same length
        min_length = min(plp1.shape[1], plp2.shape[1])
        plp1 = plp1[:, :min_length]
        plp2 = plp2[:, :min_length]

        # Calculate Euclidean distance
        distance = np.sqrt(np.mean((plp1 - plp2)**2))
        return distance



#########################################

import numpy as np
from typing import List

class ChordSimilarityDistance:
    def __init__(self):
        # Définition des 12 classes de hauteur (pitch classes)
        self.pitch_classes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def _chord_to_vector(self, chord: List[str]) -> np.ndarray:
        """Convertit un accord en vecteur binaire de 12 dimensions."""
        vector = np.zeros(12)
        for note in chord:
            index = self.pitch_classes.index(note)
            vector[index] = 1
        return vector

    def calculate_distance(self, chord1: List[str], chord2: List[str]) -> float:
        """
        Calcule la distance de similarité entre deux accords.

        Args:
            chord1 (List[str]): Premier accord (liste de noms de notes).
            chord2 (List[str]): Deuxième accord (liste de noms de notes).

        Returns:
            float: Distance de similarité entre les deux accords.
        """
        vector1 = self._chord_to_vector(chord1)
        vector2 = self._chord_to_vector(chord2)
        
        # Calcul de la distance cosinus
        similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        distance = 1 - similarity
        
        return distance
#######################################
import re
from typing import List

class SpeechRecognitionErrorRate:
    def __init__(self):
        pass

    def _preprocess(self, text: str) -> List[str]:
        """Prétraite le texte en le convertissant en minuscules et en le divisant en mots."""
        return re.findall(r'\w+', text.lower())

    def calculate_wer(self, reference: str, hypothesis: str) -> float:
        """
        Calcule le taux d'erreur de mots (WER) entre la référence et l'hypothèse.

        Args:
            reference (str): La transcription de référence.
            hypothesis (str): La transcription hypothétique générée par le système de reconnaissance vocale.

        Returns:
            float: Le taux d'erreur de mots (WER).
        """
        ref_words = self._preprocess(reference)
        hyp_words = self._preprocess(hypothesis)

        # Calcul de la distance de Levenshtein au niveau des mots
        d = [[0] * (len(hyp_words) + 1) for _ in range(len(ref_words) + 1)]

        for i in range(len(ref_words) + 1):
            d[i][0] = i
        for j in range(len(hyp_words) + 1):
            d[0][j] = j

        for i in range(1, len(ref_words) + 1):
            for j in range(1, len(hyp_words) + 1):
                if ref_words[i-1] == hyp_words[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    substitution = d[i-1][j-1] + 1
                    insertion = d[i][j-1] + 1
                    deletion = d[i-1][j] + 1
                    d[i][j] = min(substitution, insertion, deletion)

        return d[len(ref_words)][len(hyp_words)] / len(ref_words)

##########################################
'''a recoder
import librosa
from typing import List, Tuple

class EnvironmentalSoundMatchingDistance: pb librosa demande numpy donc a refaire sans librosa!
'''

###############################################
import zlib
from typing import List

class ZlibCompressionDistance:
    def __init__(self):
        """
        Initialize the ZlibCompressionDistance class.
        """
        pass

    def _compress(self, data: bytes) -> int:
        """
        Compress data using zlib and return the compressed size.

        Args:
            data (bytes): The input data to compress.

        Returns:
            int: The size of the compressed data.
        """
        compressed_data = zlib.compress(data)
        return len(compressed_data)

    def calculate_distance(self, signal1: List[float], signal2: List[float]) -> float:
        """
        Calculate the Zlib Compression Distance between two audio signals.

        Args:
            signal1 (List[float]): The first audio signal.
            signal2 (List[float]): The second audio signal.

        Returns:
            float: The compression-based distance between the two signals.
        """
        # Convert signals to bytes
        signal1_bytes = bytes(int(x * 255) for x in signal1)  # Normalize to 0-255 and convert to bytes
        signal2_bytes = bytes(int(x * 255) for x in signal2)

        # Compress individual signals
        c_signal1 = self._compress(signal1_bytes)
        c_signal2 = self._compress(signal2_bytes)

        # Concatenate and compress combined signals
        concatenated_bytes = signal1_bytes + signal2_bytes
        c_concatenated = self._compress(concatenated_bytes)

        # Calculate the Zlib Compression Distance
        distance = (c_concatenated - min(c_signal1, c_signal2)) / max(c_signal1, c_signal2)
        
        return distance
##############################################
