#### 概要
S3バケットとの接続するツール
##### 前提
以下をAWSコンソール上で実施
```
・S3 バケットを作成
・Lambdaにpythonスクリプトをデプロイ（lambda_function.py）
・Lambda関数を実行するAPI Gatewayを作成
・LambdaからS3バケットを操作するための、IAMポリシーを設定
```
#### 実現内容
##### lambda_function.py
```
・Lambda関数を作成し、デプロイ
・Presigned URL を生成
・json形式で返却
・Presigned URL の生成には、boto3クラスのclientメソッドを使用
```
##### client_function.py
```
・get_presigned_urlメソッド
　　presignedURLを取得するメソッド
　　API Gatewayで指定したLambda関数へアクセスする。
・upload_imageメソッド
　　引数で受け取った画像ファイルをS3へ送信する。
```

#### クライアントからの実行方法
##### 以下のpythonスクリプトを実行
```
$ cd [プロジェクトルート]
$ ./aws-lambda-s3-presigned-url/src/client_function.py
```
##### 実行結果
```
~/workspace$ /usr/bin/python3 ./aws-lambda-s3-presigned-url/src/client_function.py
Presigned URL obtained:
https://7110-mybucket-9dd968df-ba1a-1cab-c01c-612410b09e42.s3.amazonaws.com/test-image.jpg?AWSAccessKeyId=ASIAWMFUPQKDGYBGNKW6&Signature=jdrx95wVPB41dnhMZQo%2Fg0di%2FMU%3D&content-type=image%2Fjpeg&x-amz-security-token=IQoJb3JpZ2luX2VjEDIaDmFwLXNvdXRoZWFzdC0yIkgwRgIhAMSJiUvVMNwofn15xhp7lMUmeqTgBA06brxeOsimE2iJAiEAkjfQl2%2Ffup%2F0rR6mfD0%2BxYQ6AMQQB5qpH984BKt%2Brw8qmAMIWxAAGgw0Mzg0NjUxNjgwMDYiDN18yf3i23gJC2klByr1AgpqsAPRvkCPF6Uvw58MtRp%2ByDUAVFg185LR8IqiWuggoO41DC%2FMjdDn%2BvJDQvTpZ%2FHtyIfdUUJNv%2BgR3xTLxso8dnhTaPFpbdTlE1JDYVFHj7rkaXEkoiS3n2daQ8Pid6bg%2BGkM5Ezwlb4FzSbnN4sl6Bxi4y%2F2I1diD5gM3LsoTEFCyMDqbRc4kfY05QykMiVZSGyWw31kacz5j6VVnM9dlAfSMCy61YlvACwHKkLpkOS%2Fn9aGhCTUgtIvM9hqv4Qysyoheo%2BNrij0WzRqZj%2BTVzcxQe0bIp4uYBRM9pMKUV6hjmeRe5OXbkppKMSVwEIh7TeCNYRNQL%2FQRlaE1j6uIIxVPWZ9XcwebnkiXQKAhRm%2BDPhEu2c1vuSudD35Aip1E%2FkxxsipjnJ6flzFMHal1OAXrAYpDMqg%2BPs7FvJcL48gLsI%2FPgZhtiR0FA0NTCRpkPmaHBwZcmVgvefCtNK%2B2Hd7SDcATNMd09dKvvoKeQxBs70w3OvGvQY6nAFoSVcK5YUwGQ4oLvW9AtFQ448ngA38X2BYCc3MEr46jK8ZLTmMMwBK44izvfBaidXOhTa2t7WxRQEIlUnJPTz5qgKmUF4TU7LPJ6FrLzRsQgbvcshdMNwefbCjhdqgq5jdcB4ctrAKfsCahbBg2wzCARJ8X0yuagJQ8P0CVv63UcqM2Ldau35QujsZ%2FgrRNQlEOk3s1HXREptQkZQ%3D&Expires=1739703276
Image upload succeeded!
```
実行後、S3に該当のイメージファイルが格納されていることを確認。

##### ※画像の指定方法
pythonスクリプト内の以下の項目に画像のパス・ファイル名を指定
```
# S3 に保存するファイル名（API に渡すパラメータ）
file_name = 【ファイル名】
# アップロードするローカルの画像ファイルのパス
file_path =  r"【ファイルパス】"
```

##### 今後やること
・client_function.pyの読み取り
```
なぜget_presigned_urlメソッドでfile_nameをもらわなければいけないか忘れた。
Readmeの追記/AWSの操作系
```
