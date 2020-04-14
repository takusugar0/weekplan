Weekplan（製作中）
====

自分のなりたい姿になるために、週ごとに自分の役割を決め、それに沿った予定を立てるためのアプリ。
  
## 概要
「[7つの習慣](https://www.amazon.co.jp/%E5%AE%8C%E8%A8%B3-7%E3%81%A4%E3%81%AE%E7%BF%92%E6%85%A3-%E4%BA%BA%E6%A0%BC%E4%B8%BB%E7%BE%A9%E3%81%AE%E5%9B%9E%E5%BE%A9-%E3%82%B9%E3%83%86%E3%82%A3%E3%83%BC%E3%83%96%E3%83%B3%E3%83%BBR%E3%83%BB%E3%82%B3%E3%83%B4%E3%82%A3%E3%83%BC/dp/4863940246)」という世界的なベストセラー本から着想を得て作成したものです。    
  
このアプリは、理想の自分になるための7つの習慣のうち、  
第2の習慣として紹介されている「目的を持って始める」、  
第3の習慣として紹介されている「最優先事項を優先する」、   
を実行するのを手助けするアプリとなっています。  
  
このアプリで週ごとに理想の自分になるための自分の役割をいくつか決定しそれに沿って予定を立てることによって、重要でないタスクに振り回されず優先事項からとりかかることができます。

## Requirement
- docker  
- docker-compose

## 実行

`$ git clone git@github.com:takusugar0/weekplan.git`  
`$ cd weekplan`  
`$ docker-compose up --build`  

ブラウザで localhost:8000/roles/1/tasks にアクセス

## 残りのやること
- apiでgoogle calenderと連携
- AWSを利用してデプロイ
