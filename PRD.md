这里提供一个python服务，用来介绍告警数据的回调流程；框架为fastapi，使用python3.12
1、提供一个处理订阅告警的接口/callback/alarm  
接受参数是json格式，格式如下：
```
{
  "SubscribeListObject": {
    "SubscribeObject": [
      {
        "SubscribeID": "20230101000000000001",
        "Title": "订阅样例-订阅整个视图库过车",
        "ApplicantName": "kedacom",
        "ApplicantOrg": "kedacom",
        "SubscribeDetail": "13",
        "BeginTime": "20230110110000",
        "EndTime": "20991015113400",
        "ReceiveAddr": "http://127.5.6.2:8080/VIID/SubscribeNotifications",
        "ResourceClass": 4,
        "ResourceURI": "视图库ServerID",
        "ResultImageDeclare":"-1",
        "ResultFeatureDeclare":"-1"
      }
    ]
  }
}
```
2、当访问该接口时候，把请求参数数据写入txt文件