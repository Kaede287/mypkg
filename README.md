# mypkg
[![test](https://github.com/Kaede287/mypkg2/actions/workflows/test.yml/badge.svg)](https://github.com/Kaede287/mypkg2/actions/workflows/test.yml)

## /countdownトピックの説明

* Int16型のメッセージをパブリッシュ及びサブスクライブするトピックです.

### talkerについての説明

* 1秒ごとに整数をカウントダウンを行い, /countdownトピックにメッセージをパブリッシュするノードです.

### listenerについての説明

* /countdownトピックからメッセージを受け取り, 受け取ったメッセージが5で割り切れる数整のとき, 残りの秒数を表示する. 受け取ったメッセージが奇数か偶数かを判定し, 表示を行うノードです.

## 実行方法

任意のディレクトリに移動し, ビルドを行ってください.

```
$ cd ~/ros2_ws
$ colcon build
$ source ~/.bashrc
```
ディレクトリを変更し, 2つの端末を使って実行してください.

 * 端末1 (talker)

```
$ cd ~/ros2_ws
$ ros2 run mypkg talker
```

 * 端末2 (listener)

```
$ cd ~/ros2_ws
$ ros2 run mypkg listener
```

## 実行結果 (listener)

```
[INFO] [1703395208.554193644] [listener]: 残り 1965 です
[INFO] [1703395208.555903104] [listener]: Listen: 1965 奇数です
[INFO] [1703395209.024968396] [listener]: Listen: 1964 偶数です
[INFO] [1703395209.525325903] [listener]: Listen: 1963 奇数です
[INFO] [1703395210.025050499] [listener]: Listen: 1962 偶数です
[INFO] [1703395210.524841052] [listener]: Listen: 1961 奇数です
[INFO] [1703395211.024602419] [listener]: 残り 1960 です
[INFO] [1703395211.025719526] [listener]: Listen: 1960 偶数です
[INFO] [1703395211.524676304] [listener]: Listen: 1959 奇数です
[INFO] [1703395212.024778984] [listener]: Listen: 1958 偶数です
[INFO] [1703395212.524473973] [listener]: Listen: 1957 奇数です
[INFO] [1703395213.024377282] [listener]: Listen: 1956 偶数です
[INFO] [1703395213.524324083] [listener]: 残り 1955 です
```

## テスト環境
* Ubuntu20.04

* テスト完了には30秒を要します. 

## 必要なソフトウェア
* ros2

* python
    * テスト済み 3.7～3.10

## ライセンス関係
* このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
* このパッケージのコードは, 下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）の一部のものを加筆し, 本人の許可を得て自身の著作としたものです.
        * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

©2023 Kaede Ichikawa
