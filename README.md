# 概要

Gowin RUNBER向けCH552T用JTAGファームウェア (Erase Flash修正版)

[オリジナルのCH552T用JTAGファームウェア](https://github.com/diodep/ch55x_jtag) に対して、Gowin RUNBERに搭載されている `GW1N-LV4` 向けのErase Flashが成功するようにする修正を入れたものです。

対策としては `Erase Flash` のみですので、 **実際にFlashに書き込むことは依然できません。** あくまでErase FlashによりSRAMにすら書き込めなくなった状態から復帰する・誤ってFlash書き込みを行った場合に書き込めなくなるのを防止する効果があるだけです。

# 使い方

`python3` がインストールされている環境で以下の手順を実行します。

1. 必要なパッケージをインストールする

```
$ sudo python3 -mpip install pyusb ch55xtool
```

2. Gowin RUNBERをPCに接続する
3. このリポジトリのルートにある `to_dfu.py` を実行する

```
$ python3 to_dfu.py
Apply magic success.
..CH552 is now in DFU mode.
```

4. `ch55xtool` を使ってCH552Tのファームウェアを更新する。

```
$ sudo ch55xtool -f usb_jtag.bin -r
```

5. 書き込みが完了したら、Gowin RUNBERをUSBポートから取り外して再度接続する。
6. GOWIN ProgrammerからErase Flashを実行する。