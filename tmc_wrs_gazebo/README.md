gazeboのsdfを、usdに変換しました。[https://github.com/kokhayas/sdf2usd_env]
tmc_wrs_gazebo_worlds/models/*/output.usd
に、変換後のoutput.usdが入っています。
isaac simで開く時に,
1. Looksのmaterials/textureのpathが正しいか確認する必要があります。defaultでisaac simはmaterials/texture/*.pngを見に行きます。場合により、mesh/*.pngのpathに書き換える必要があります。*.pngがない場合は、一色のobjectなので、issac sim上でrgbを指定します。
2. scaleを100倍にする必要があります。

# tmc_wrs_gazebo

## LICENSE

This software except object models is released under the BSD 3-Clause Clear License, see LICENSE.txt.

Regarding the license of object models, see README.md in the tmc_wrs_gazebo_worlds package.
