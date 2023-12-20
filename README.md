# ros2
[![test](https://github.com/Kaede287/mypkg2/actions/workflows/test.yml/badge.svg)](https://github.com/Kaede287/mypkg2/actions/workflows/test.yml)

## トピックについての説明

* パブリッシャー(talker)が動いてから何秒経過したかの数を表示します.

### パブリッシャー(talker)についての説明

* 1秒ごとに整数をカウントダウンしてトピックにメッセージをパブリッシュするノードです.

### サブスクライバー(listener)についての説明

* トピックからメッセージを受け取り、5で割り切れる数整の時,残りの秒数を表示します. 

## 実行方法

任意のディレクトリに移動し,ビルドを行ってください.

```
$ cd ~/[ディレクトリ名]
$ colcon build
$ source ~/.bashrc
```
ディレクトリを変更し,2つの端末を使って実行してください.

 * 端末1 (talker)

```
$ cd ~/[ディレクトリ名]
$ ros2 run mypkg talker
```

 * 端末2 (listener)

```
$ cd ~/[ディレクトリ名]
$ ros2 run mypkg listener
```

## テスト環境
* Ubuntu20.04

## 必要なソフトウェア
* ros2

* python
    * テスト済み

## ライセンス関係
* このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
* このパッケージのコードは, 下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）の一部を本人の許可を得て自身の著作としたものです.
        * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

©2023 Kaede Ichikawa
