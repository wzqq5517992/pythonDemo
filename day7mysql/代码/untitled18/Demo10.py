#coding:utf8

#拓展内容  阿里鉴黄



from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkgreen.request.v20180509 import ImageSyncScanRequest
import json
import uuid
import datetime
def jianhuang(url,type=['porn'],accessKeyId='LTAIbdu14y5Gkx78',accessKeySecret='XUKhoYSTjieG8awm3tVzv41GxXRTiM'):
    if accessKeyId =='' or accessKeySecret=='':
        print('请去阿里注册获得accessKeyId和accessKeySecret')
    # 请替换成您自己的accessKeyId、accessKeySecret。您可以修改aliyun.ak.conf配置文件，也可以直接明文替换。
    clt = client.AcsClient(accessKeyId, accessKeySecret, 'cn-shanghai')
    region_provider.modify_point('Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
    request = ImageSyncScanRequest.ImageSyncScanRequest()
    request.set_accept_format('JSON')
    # 同步检测只支持对单张图片进行检测，即只有一个task
    task1 = {"dataId": str(uuid.uuid1()),
             "url":url,
             "time": datetime.datetime.now().microsecond
             }
    request.set_content(json.dumps({"tasks": [task1], "scenes": type}))
    response = clt.do_action(request)
    print(response)
    result = json.loads(response)
    if 200 == result["code"]:
        taskResults = result["data"]
        for taskResult in taskResults:
            if (200 == taskResult["code"]):
                sceneResults = taskResult["results"]
                for sceneResult in sceneResults:
                    scene = sceneResult["scene"]
                    suggestion = sceneResult["suggestion"]
                    print(suggestion)
                    print(scene)
                    print("图片标准", sceneResult['label'], '置信度', str(sceneResult['rate']), '建议',
                          sceneResult['suggestion'])
                    # 根据scene和suggetion做相关处理
                    # do something
    return result

x=jianhuang("https://zcpicture.oss-cn-hangzhou.aliyuncs.com/mmonlypic/0015535d2ed41aae828d3cdbdbd25186.jpg")
print(x)
z=jianhuang("https://zcpicture.oss-cn-hangzhou.aliyuncs.com/mmonlypic/000b57878a64ab18c5b88a0cdb07cb9d.jpg")
print(z)