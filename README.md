# mypkg
[![test](https://github.com/Kaede287/mypkg2/actions/workflows/test.yml/badge.svg)](https://github.com/Kaede287/mypkg2/actions/workflows/test.yml)

## トピックについての説明

* talkerが動いてから何秒経過したかの数を表示します.

### talkerについての説明

* 1秒ごとに整数をカウントダウンしてトピックにメッセージをパブリッシュするノードです.

### listenerについての説明

* トピックからメッセージを受け取り, 5で割り切れる数整のとき, 残りの秒数を表示します. 

## 実行方法

任意のディレクトリに移動し, ビルドを行ってください.

```
$ cd ~/ros2_ws/src/mypkg
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
[INFO] [1703053612.502074349] [listener]: 残り 1990 です
[INFO] [1703053612.503366912] [listener]: Listen: 1990
[INFO] [1703053613.479890584] [listener]: Listen: 1989
[INFO] [1703053614.487503632] [listener]: Listen: 1988
[INFO] [1703053615.480155033] [listener]: Listen: 1987
[INFO] [1703053616.479768981] [listener]: Listen: 1986
[INFO] [1703053617.479619983] [listener]: 残り 1985 です
[INFO] [1703053617.480615968] [listener]: Listen: 1985
[INFO] [1703053618.480008503] [listener]: Listen: 1984
[INFO] [1703053619.479740386] [listener]: Listen: 1983
[INFO] [1703053620.479840304] [listener]: Listen: 1982
[INFO] [1703053621.484086272] [listener]: Listen: 1981
```

## テスト環境
* Ubuntu20.04

## 必要なソフトウェア
* ros2

* python
    * テスト済み 3.7～3.10

## ライセンス関係
* このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
* このパッケージのコードは, 下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）の一部を本人の許可を得て自身の著作としたものです.
        * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

©2023 Kaede Ichikawa
