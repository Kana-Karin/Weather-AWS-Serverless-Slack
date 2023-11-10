# Weather-AWS-Serverless-Slack
毎朝8:30分に北海道地方の天気予報をSlackのチャンネルに通知するサーバーレスアプリ
<br>気象庁APIを利用させていただいています。

## アーキテクチャ図
![Weather-AWS-Serverless](https://github.com/Kana-Karin/Weather-AWS-Serverless-Slack/assets/84316229/54f6bcc3-1d49-4560-91ac-4e38144bf664)
<br>EventBridgeのスケジューラーを利用して、Lambda関数を定期的に実行

## Lambda関数実行後、Slackチャンネルへ投稿
<img width="657" alt="スクリーンショット 2023-11-10 19 33 00" src="https://github.com/Kana-Karin/Weather-AWS-Serverless-Slack/assets/84316229/38ff2010-4147-47f9-a2cf-01832854347a">
