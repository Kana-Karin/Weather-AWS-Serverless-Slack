# Weather-AWS-Serverless-Slack
毎朝8:30分に北海道地方の天気予報をSlackのチャンネルに通知するサーバーレスアプリ
<br>気象庁APIを利用させていただいています。

## アーキテクチャ図
![Weather-AWS-Serverless](https://github.com/Kana-Karin/Weather-AWS-Serverless-Slack/assets/84316229/54f6bcc3-1d49-4560-91ac-4e38144bf664)
<br>EventBridgeのスケジューラーを利用して、Lambda関数を定期的に実行

## Lambda関数実行後、Slackチャンネルへ投稿
<img width="657" alt="スクリーンショット 2023-11-10 19 33 00" src="https://github.com/Kana-Karin/Weather-AWS-Serverless-Slack/assets/84316229/38ff2010-4147-47f9-a2cf-01832854347a">

### つまづいた部分
- EventBridgeからLambda関数をトリガーする際、Lambda関数の実行ロール、EventBridgeにassumeが上手く付与出来ていなかった
- EventBridgeにてcronを設定する際、最初に`30 8 * * * *`(毎朝8:30分)でパターンを構築したが、「CRON 式が無効です」が表示された<br>
対処方法としてはAWS公式リファレンスを参照し`cron 式の日フィールドと曜日フィールドを同時に指定することはできません。一方のフィールドに値 (または *) を指定する場合、もう一方のフィールドで ? (疑問符) を使用する必要があります。`とのことでした

### 参考にさせていただいたサイト
[Developers.IO](https://dev.classmethod.jp/articles/tsnote-eventbridge-cron-expression-is-invalid-in-eventbridge-schedule-pattern/)
[Qiita](https://qiita.com/miriwo/items/0331b7277a819c05ed4b)
