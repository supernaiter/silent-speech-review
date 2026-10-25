# サイレントスピーチ・インタフェース論文レビュー

サイレントスピーチ・インタフェース（SSI）の論文 **132本** を、結果がどの条件で測られたかと一緒にレビューしています。管理：[木村直紀](https://nao-ki-mura.com/ja/)（[ORCID](https://orcid.org/0000-0001-9167-1923)）。最終更新 2026-10-19。

SSIの精度は、語彙の大きさ、話者依存か、別日に付け直して測ったか、オンラインで動かしたかで大きく変わります。このレビューは、各論文の主な数字の横にこれらの条件を並べます。英語の比較表は [README](README.md) にあります。各論文のページには、英語の要約と評価条件の下に全文レビュー（日本語または英語）があります。

## センサ別の本数

- [サーベイ](README.md#surveys)：4本
- [口蓋電極（EPG）・口腔内センサ](README.md#electropalatography--in-mouth-sensors)：1本
- [超音波・舌の画像](README.md#ultrasound--tongue-imaging)：18本
- [表面筋電（EMG）](README.md#surface-emg)：25本
- [脳信号（EEG・MEG・皮質内）](README.md#brain-signals-eeg-meg-intracortical)：29本
- [レーダー・電波・Wi-Fi](README.md#radar-rf--wi-fi)：5本
- [唇・顔の映像](README.md#lip--face-video)：43本
- [音響・ささやき・装着型の動きセンサ](README.md#acoustic-whisper--wearable-motion-sensors)：7本

## 最初に読む論文

1. [Silent Speech Interfaces in the Era of Large Language Models: A Comprehensive Taxonomy and Systematic Review](reviews/silent-speech-interfaces-in-the-era-of-large-language-models-a-comprehensive-taxonomy-and-system.md)（2026）A broad and useful SSI taxonomy, but missing review-selection detail and concrete citation errors make its benchmark tables unsuitable for unverified rankings or deployment claims.
2. [Silent Speech Interfaces for Speech Restoration: A Review](reviews/silent-speech-interfaces-for-speech-restoration-a-review.md)（2020）Core SSI survey with concrete deployment constraints.
3. [Digital Voicing of Silent Speech](reviews/digital-voicing-of-silent-speech.md)（2020）Core EMG SSI paper with real gains from target transfer.
4. [SottoVoce: An Ultrasound Imaging-Based Silent Speech Interaction Using Deep Neural Networks](reviews/sottovoce.md)（2019）A solid proof of concept that reconstructs speech audio from ultrasound for controlling unmodified smart speakers, showcasing important system design insight despite prototype limitations in latency, hardware bulk, and speaker dependency.
5. [SilentSpeller: Towards mobile, hands-free, silent speech text entry using electropalatography](reviews/silentspeller.md)（2022）SilentSpeller is a strong, rigorously tested SSI system that reframes silent speech as silent spelling, enabling large vocabulary, live text entry, and walking robustness with in-mouth electropalatography sensors.
6. [LipLearner: Customizable Silent Speech Interactions on Mobile Devices](reviews/liplearner-customizable-silent-speech-interactions-on-mobile-devices.md)（2023）LipLearner is a strong mobile silent speech system that uniquely closes the loop from few-shot lipreading model design to practical on-device customization and keyword spotting, demonstrated robustly in real-world conditions and a user study.
7. [AESSI: An Around-Ear Silent Speech Interface for Cross-Day Online Reuse without Test-Day Calibration](reviews/aessi-an-around-ear-silent-speech-interface-for-cross-day-online-reuse-without-test-day-calibrat.md)（2026）耳周囲cEEGridで25の固定中国語文を認識。テスト日較正なしの別日ホルドアウトで平均92.24%、21日以上後のライブ250試行で98.00%。開語彙会話や患者適用は未実証。
8. [Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication](reviews/reconstructing-unseen-sentences-from-speech-related-biosignals-for-open-vocabulary-neural-commun.md)（2025）Held-out sentence reconstruction is demonstrated in personalized EEG/EMG experiments, but the strongest aggregate evidence is overt/whispered phoneme decoding—not unrestricted imagined-speech communication.
9. [Updating the silent speech challenge benchmark with deep learning](reviews/updating-the-silent-speech-challenge-benchmark-with-deep-learning.md)（2017）Benchmark update with a real, reproducible WER gain.

## 論文の追加と誤りの報告

Issue で受け付けています（[論文の追加](https://github.com/supernaiter/silent-speech-review/issues/new?template=add-paper.yml)、[誤りの報告](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml)）。
