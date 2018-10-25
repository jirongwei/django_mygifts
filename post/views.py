from django.http import JsonResponse,HttpResponse
import time,json
from . import models
import user.models

# personal首页
def personal(request):

    return HttpResponse('i am post')

# 根据id获取用户信息
def getUserInfo(request):
    pass

# update用户信息
def updateUserInfo(request):
    pass

# upload头像
def uploadIcon(request):
    pass

# 安全等级
def securityLevel(request):
    pass

# 修改密码
def updatePwd(request):
    pass

# 绑定手机
def bindPhone(request):
    pass

# 收藏-->展示
def getCollectList(request):
    if request.method=='GET':
        # 前端传来收藏的用户id
        uid=request.GET.get('u_id')
        # 这里定义一个空列表，将后面遍历出来的数据加进来
        all_result=[]
        # 通过id 查询
        colpost=models.PostCollect.objects.filter(userinfo_id=uid).values('post_id_id','id','post_id__ptitle','post_id__pbriefcont')
        print(colpost)
        # 将查询到的结果遍历出来
        for col in colpost:
            # 获取里面的收藏的文章的ID
            pe_id=col['post_id_id']
            # 根据文章id查找用户id
            collect=models.PostCollect.objects.filter(post_id_id=pe_id).values()
            # print(collect)
            # 将查出来的用户id通过.count计算出来个数
            col['coll_count']=collect.count()
            # 在插入到列表中
            all_result.append(col)
        return HttpResponse(json.dumps(list(all_result),ensure_ascii=False))


# 收藏-->详情
def getCollectDetail(request):
    pass

# 收藏-->删除
def delCollect(request):
    pass

# 订单展示
def getOrderList(request):
    pass

# 订单详情
def getOrderDetail(request):
    pass

# 地址管理
def getAddressList(request):
    pass

# 添加地址
def addAddress(request):
    pass

# 修改地址
def updateAddress(request):
    pass

# 插入帖子
def createPost(request):
    pid=list(user.models.UserInfo.objects.all())

    # pid=list(user.models.UserInfo.objects.all()[0,1].values("id"))
    post=[
        {
            "ptitle":"面试想拿 10K，HR 说你只值 7K，该怎样回答或者反驳？",
            "ptitleimg":"",
            "pdetailcont":"<p>谢邀。</p><p><br></p><p>题主和题主朋友还是太年轻，其实这道题很简单的啊，别搞得太复杂了。</p><p><br></p><p>正确的做法是：</p><p><br></p><p>不动声色，继续跟HR谈下去、把面试流程走完，并且争取拿到这个7K的offer。</p><p><br></p><p>这里有一个小技巧：</p><p><br></p><p>如果拿到offer，礼貌地跟HR表示感谢，不过不要马上入职。可以找个由头，比方说自己需要考虑一下、最近有私事要处理，等等。给自己争取一段缓冲的时间，别太长，十天左右差不多就可以了。</p><p><br></p><p>有了offer保底，接下来就好办了。</p><p><br></p><p>利用缓冲期，抓紧时间再多面几家，如果有更好的offer，就“人往高处走”；如果没有，就老老实实回来，到这家7K的公司入职，再作打算。</p><p><br></p><p>入职之后肯定有试用期的嘛，还可以“骑驴找马”啊，但关键是要先把“驴”给骑上，“家里有粮、心中不慌”。</p><p><br></p><p>当然，要是你竞争力特别强、有好多公司争着要，那就用不着“骑驴”了，直接“找马”就成。</p><p><br></p><p>不过，绝大多数人应该都没有那个底气吧，所以还是务实一点的好。</p><p><br></p><p>——————   分割线  ——————</p><p><br></p><p>最后讲一个彩蛋吧。</p><p><br></p><p>是以前公司的事。当时老板打算拓展新业务，于是就让HR招人。可能是广告上把公司吹得太玄乎了，岗位描述也是各种高大上，一不小心来了个猛人应聘。</p><p><br></p><p>此人是TOP2的研究生，30出头，工作经验也有，还在500强干过。简历一拿过来，把HR吓坏了，直接跑去问老板怎么办。</p><p><br></p><p>过了一会儿，HR从老板办公室回来。之后的面试过程，HR抖擞精神、底气十足，对老板、对公司、对新业务各种吹嘘，连“计划5年内上市”这种话都飚出来了，当时我在旁边，差点没憋住笑。猛人也是频频点头表示很有兴趣，一边展示自身实力、一边表态愿意加入。等谈到薪资的时候，HR先是画了一堆大饼，最后开出的价码是：</p><p><br></p><p>月薪3000。</p><p><br></p><p>是的，你没有看错。而且试用期三个月，转正之前打八折。</p><p><br></p><p>猛人瞬间就懵逼了，表示要考虑考虑。第二天打来电话，婉拒offer。</p><p><br></p><p>包括我们在内，也都松了一口气。还好猛人没有当场答应，不然大家都很尴尬、不好收场啊。</p><p><br></p><p>回头老板把HR臭骂了一通，招聘广告全部重写，岗位头衔也从“高级经理”变成了“业务专员”。</p><p><br></p><p>——————   二次分割线  ——————</p><p><br></p><p>随手写的回答，没想到能引起这么大的动静，看来大家对于面试的话题还是很感兴趣的。</p><p><br></p><p>多说两句，顺带着也回应一些朋友的疑问：</p><p><br></p><p>公司还在，发展得怎么样不清楚，不过听说老板后来又开了两、三家公司，应该是赚到钱了；</p><p><br></p><p>HR也还在，据说一路高升，做到总经理了；</p><p><br></p><p>很多朋友对于给TOP2猛人开3000块一个月的细节忿忿不平，不过这事儿老板还真干成过。有一段时间，公司招了个什么专员，跟我不是一个部门。这人是女生，个子特别高、身材也好，所以我印象很深。干了有大半年吧，走了。有一回跟HR喝酒，无意间聊起来这事儿，我开玩笑说那个模特儿走了，你怎么不把人家留住，看着也养眼啊。HR嘿嘿一笑，说老板也不想她走，但她太贪心，想钱想疯了，跟老板提出要涨工资，而且是要翻一倍。我问HR那个模特儿什么来头，敢这么要价，HR嘿嘿一笑，说人家是TOP2毕业的，还是博士。当时我就惊了，手里的半根烤串儿都差点儿掉地下。我说你们到底给人家开多少工钱啊，HR嘿嘿一笑，从桌上拿起三根签子，在我面前比划了一番。</p><p><br></p><p>我当时心里只有三个字：</p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p>人！才！啊！</p><p><br></p><p>—————— 三次分割线（顺便纪念点赞数上10K） ——————</p><p><br></p><p>哎呦，一不留神，点赞居然过万了，有点碉堡了哦！</p><p><br></p><p>本来只打算给年轻的朋友们提供一点小思路，没想到居然有这么多人认同，说实话，作为一枚油腻的中年大叔，俺还是有点意外的。我以为这招“骑驴找马”应该算求职常识、只不过是基本操作而已，结果还是有许多网友表示不能接受，唉，叔真是既羡慕你们的青春、又疼爱你们的单纯啊！</p><p><br></p><p>承蒙大家捧场，俺就再多唠叨几句吧。</p><p><br></p><p>【关于真假】</p><p><br></p><p>我看了评论，数量不多、大概有十几位网友吧，表示认同我写的内容。他们相信、理解我说的东西，也有过类似的经历，我很欣慰。这说明留言的大多数网友要么年纪太小、太理想化，要么阅历单薄、没怎么见识过社会的另一面。</p><p><br></p><p>怎么说呢，我倒是希望大家都能顺利进入高大上的公司，用不着跟我前老板和HR那样的人打交道。至于我说的呢，信不信随你。中国那么大，什么样的人没有啊？大家不妨先留个印象，万一你将来遇到类似的情况呢？</p><p><br></p><p>等你也像我一样上了年纪，你就会明白：生活永远比故事更狗血、更精彩。见的多了、经历的多了，段子什么的，还需要花心思现编么？切。</p><p><br></p><p>【关于模特女博士】</p><p><br></p><p>HR的意思很明确，就是3K的月薪。大伙儿也别太把TOP2啦、博士啊这些标签当回事儿了，具体情况要具体分析。</p><p><br></p><p>首先，这个女博士硬件确实好，至于为什么会被忽悠过来，我也不大清楚，但人家来了就是来了。</p><p><br></p><p>其次，我说她身材好，主要是说身高。一个是高、再一个是瘦，不过呢，颜值方面确实比较拖后腿，所以说老天爷还是公平的；而且她是文科，再加上年龄也不小，我估计想找理想的工作也不太容易吧。</p><p><br></p><p>最后，她这个案例有一定的特殊性，属于可遇不可求的小概率事件，反正我也只见过这么一回，应该不具备可复制性。那些留言表示羡慕的同学，我只能说天上掉下来馅饼，让老板给捡着了。</p><p><br></p><p>【关于HR】</p><p><br></p><p>HR是不是人才，我看大家还有分歧；但如果说他是个人精，你们肯定举双手双脚赞成。这哥们儿貌似连大专文凭都没有，但是特别圆滑、会来事儿。他绝对是属于那种人 ——</p><p><br></p><p>你如果是员工，你怎么瞅他都不顺眼、但当着他面你又没脾气；</p><p>你如果是老板，你100%希望自己手底下也有这么号人物、用起来特顺手。</p><p><br></p><p>强行类比的话，大概是一个小公司版本的和珅吧。</p><p><br></p><p>所以公司发展、他也沾光；老板发达、他就跟着一路高升，这没毛病吧？</p><p><br></p><p>【关于公司和老板】</p><p><br></p><p>有人觉得low、不上档次，但我敢说，绝大部分的公司，可能还不如它。</p><p><br></p><p>好歹是在一线城市、而且是中心区办公；</p><p>好歹解决了几百号人的就业问题；</p><p>好歹是在做实业、产供销一条龙；</p><p>好歹基本上遵守劳动法，该给的都给。当然，工资低是另一码事了；</p><p>好歹办了有二十多年了，貌似国内的中小企业平均寿命也就是3、4年的样子吧？</p><p><br></p><p>其实老板也有一颗上进的心。有一回快过节了，我陪老板一起去gov部门，嗯、你懂得。事情办完了，老板跟人家简单聊了几句，无意间感叹说希望gov多给点儿扶持、他想把业务再拓展拓展，人家半开玩笑地轻轻怼了回来，大意是说 ——</p><p><br></p><p>差不多就得啦。像你们这样的企业，还活着、能挣着钱、年年过节我都见得到，比上不足、比下绰绰有余，已经算是很好的了。</p><p><br></p><p>老板当时还有些惊讶：我这样的穷光蛋也能算“很好”？跟那些身家多少多少亿的成功人士比起来，还差得远呢！不过后来，他好像也转过弯来了，毕竟“人比人气死人”嘛！</p><p><br></p><p>我写这些的意思是说：不是只有500强才叫公司。绝大部分的工作岗位，是由那些看上去很low、不上档次的“500弱”们提供的。很多时候，能在50000强里混个饭碗，就已经很不错了。</p>",
            "pbriefcont":"上官文商： 谢邀。 题主和题主朋友还是太年轻，其实这道题很简单的啊，别搞得太复杂了。 正确的做法是： 不动声色，继续跟HR谈下去、把面试流程走完，并且争取拿…",
            "p_createtime":time.time(),
            "p_userid":pid[0]
        },
        {
            "ptitle": "K，该怎样回答或者反驳？",
            "ptitleimg": "",
            "pdetailcont": "<p>题主和题主朋友还是太年轻，其实这道题很简单的啊，别搞得太复杂了。</p><p><br></p><p>正确的做法是：</p><p><br></p><p>不动声色，继续跟HR谈下去、把面试流程走完，并且争取拿到这个7K的offer。</p><p><br></p><p>这里有一个小技巧：</p><p><br></p><p>如果拿到offer，礼貌地跟HR表示感谢，不过不要马上入职。可以找个由头，比方说自己需要考虑一下、最近有私事要处理，等等。给自己争取一段缓冲的时间，别太长，十天左右差不多就可以了。</p><p><br></p><p>有了offer保底，接下来就好办了。</p><p><br></p><p>利用缓冲期，抓紧时间再多面几家，如果有更好的offer，就“人往高处走”；如果没有，就老老实实回来，到这家7K的公司入职，再作打算。</p><p><br></p><p>入职之后肯定有试用期的嘛，还可以“骑驴找马”啊，但关键是要先把“驴”给骑上，“家里有粮、心中不慌”。</p><p><br></p><p>当然，要是你竞争力特别强、有好多公司争着要，那就用不着“骑驴”了，直接“找马”就成。</p><p><br></p><p>不过，绝大多数人应该都没有那个底气吧，所以还是务实一点的好。</p><p><br></p><p>——————   分割线  ——————</p><p><br></p><p>最后讲一个彩蛋吧。</p><p><br></p><p>是以前公司的事。当时老板打算拓展新业务，于是就让HR招人。可能是广告上把公司吹得太玄乎了，岗位描述也是各种高大上，一不小心来了个猛人应聘。</p><p><br></p><p>此人是TOP2的研究生，30出头，工作经验也有，还在500强干过。简历一拿过来，把HR吓坏了，直接跑去问老板怎么办。</p><p><br></p><p>过了一会儿，HR从老板办公室回来。之后的面试过程，HR抖擞精神、底气十足，对老板、对公司、对新业务各种吹嘘，连“计划5年内上市”这种话都飚出来了，当时我在旁边，差点没憋住笑。猛人也是频频点头表示很有兴趣，一边展示自身实力、一边表态愿意加入。等谈到薪资的时候，HR先是画了一堆大饼，最后开出的价码是：</p><p><br></p><p>月薪3000。</p><p><br></p><p>是的，你没有看错。而且试用期三个月，转正之前打八折。</p><p><br></p><p>猛人瞬间就懵逼了，表示要考虑考虑。第二天打来电话，婉拒offer。</p><p><br></p><p>包括我们在内，也都松了一口气。还好猛人没有当场答应，不然大家都很尴尬、不好收场啊。</p><p><br></p><p>回头老板把HR臭骂了一通，招聘广告全部重写，岗位头衔也从“高级经理”变成了“业务专员”。</p><p><br></p><p>——————   二次分割线  ——————</p><p><br></p><p>随手写的回答，没想到能引起这么大的动静，看来大家对于面试的话题还是很感兴趣的。</p><p><br></p><p>多说两句，顺带着也回应一些朋友的疑问：</p><p><br></p><p>公司还在，发展得怎么样不清楚，不过听说老板后来又开了两、三家公司，应该是赚到钱了；</p><p><br></p><p>HR也还在，据说一路高升，做到总经理了；</p><p><br></p><p>很多朋友对于给TOP2猛人开3000块一个月的细节忿忿不平，不过这事儿老板还真干成过。有一段时间，公司招了个什么专员，跟我不是一个部门。这人是女生，个子特别高、身材也好，所以我印象很深。干了有大半年吧，走了。有一回跟HR喝酒，无意间聊起来这事儿，我开玩笑说那个模特儿走了，你怎么不把人家留住，看着也养眼啊。HR嘿嘿一笑，说老板也不想她走，但她太贪心，想钱想疯了，跟老板提出要涨工资，而且是要翻一倍。我问HR那个模特儿什么来头，敢这么要价，HR嘿嘿一笑，说人家是TOP2毕业的，还是博士。当时我就惊了，手里的半根烤串儿都差点儿掉地下。我说你们到底给人家开多少工钱啊，HR嘿嘿一笑，从桌上拿起三根签子，在我面前比划了一番。</p><p><br></p><p>我当时心里只有三个字：</p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p><br></p><p>人！才！啊！</p><p><br></p><p>—————— 三次分割线（顺便纪念点赞数上10K） ——————</p><p><br></p><p>哎呦，一不留神，点赞居然过万了，有点碉堡了哦！</p><p><br></p><p>本来只打算给年轻的朋友们提供一点小思路，没想到居然有这么多人认同，说实话，作为一枚油腻的中年大叔，俺还是有点意外的。我以为这招“骑驴找马”应该算求职常识、只不过是基本操作而已，结果还是有许多网友表示不能接受，唉，叔真是既羡慕你们的青春、又疼爱你们的单纯啊！</p><p><br></p><p>承蒙大家捧场，俺就再多唠叨几句吧。</p><p><br></p><p>【关于真假】</p><p><br></p><p>我看了评论，数量不多、大概有十几位网友吧，表示认同我写的内容。他们相信、理解我说的东西，也有过类似的经历，我很欣慰。这说明留言的大多数网友要么年纪太小、太理想化，要么阅历单薄、没怎么见识过社会的另一面。</p><p><br></p><p>怎么说呢，我倒是希望大家都能顺利进入高大上的公司，用不着跟我前老板和HR那样的人打交道。至于我说的呢，信不信随你。中国那么大，什么样的人没有啊？大家不妨先留个印象，万一你将来遇到类似的情况呢？</p><p><br></p><p>等你也像我一样上了年纪，你就会明白：生活永远比故事更狗血、更精彩。见的多了、经历的多了，段子什么的，还需要花心思现编么？切。</p><p><br></p><p>【关于模特女博士】</p><p><br></p><p>HR的意思很明确，就是3K的月薪。大伙儿也别太把TOP2啦、博士啊这些标签当回事儿了，具体情况要具体分析。</p><p><br></p><p>首先，这个女博士硬件确实好，至于为什么会被忽悠过来，我也不大清楚，但人家来了就是来了。</p><p><br></p><p>其次，我说她身材好，主要是说身高。一个是高、再一个是瘦，不过呢，颜值方面确实比较拖后腿，所以说老天爷还是公平的；而且她是文科，再加上年龄也不小，我估计想找理想的工作也不太容易吧。</p><p><br></p><p>最后，她这个案例有一定的特殊性，属于可遇不可求的小概率事件，反正我也只见过这么一回，应该不具备可复制性。那些留言表示羡慕的同学，我只能说天上掉下来馅饼，让老板给捡着了。</p><p><br></p><p>【关于HR】</p><p><br></p><p>HR是不是人才，我看大家还有分歧；但如果说他是个人精，你们肯定举双手双脚赞成。这哥们儿貌似连大专文凭都没有，但是特别圆滑、会来事儿。他绝对是属于那种人 ——</p><p><br></p><p>你如果是员工，你怎么瞅他都不顺眼、但当着他面你又没脾气；</p><p>你如果是老板，你100%希望自己手底下也有这么号人物、用起来特顺手。</p><p><br></p><p>强行类比的话，大概是一个小公司版本的和珅吧。</p><p><br></p><p>所以公司发展、他也沾光；老板发达、他就跟着一路高升，这没毛病吧？</p><p><br></p><p>【关于公司和老板】</p><p><br></p><p>有人觉得low、不上档次，但我敢说，绝大部分的公司，可能还不如它。</p><p><br></p><p>好歹是在一线城市、而且是中心区办公；</p><p>好歹解决了几百号人的就业问题；</p><p>好歹是在做实业、产供销一条龙；</p><p>好歹基本上遵守劳动法，该给的都给。当然，工资低是另一码事了；</p><p>好歹办了有二十多年了，貌似国内的中小企业平均寿命也就是3、4年的样子吧？</p><p><br></p><p>其实老板也有一颗上进的心。有一回快过节了，我陪老板一起去gov部门，嗯、你懂得。事情办完了，老板跟人家简单聊了几句，无意间感叹说希望gov多给点儿扶持、他想把业务再拓展拓展，人家半开玩笑地轻轻怼了回来，大意是说 ——</p><p><br></p><p>差不多就得啦。像你们这样的企业，还活着、能挣着钱、年年过节我都见得到，比上不足、比下绰绰有余，已经算是很好的了。</p><p><br></p><p>老板当时还有些惊讶：我这样的穷光蛋也能算“很好”？跟那些身家多少多少亿的成功人士比起来，还差得远呢！不过后来，他好像也转过弯来了，毕竟“人比人气死人”嘛！</p><p><br></p><p>我写这些的意思是说：不是只有500强才叫公司。绝大部分的工作岗位，是由那些看上去很low、不上档次的“500弱”们提供的。很多时候，能在50000强里混个饭碗，就已经很不错了。</p>",
            "pbriefcont": "谢邀。 题主和题主朋友还是太年轻，其实这道题很简单的啊，别搞得太复杂了。 正确的做法是： 不动声色，继续跟HR谈下去、把面试流程走完，并且争取拿…",
            "p_createtime": time.time(),
            "p_userid": pid[1]
        }
    ]
    for i in post:
        pos=models.Post(**i)
        pos.save()
        print (pos.id)
    return HttpResponse({"code":"001"})

# 删除地址
def delAddress(request):
    pass

 #加载帖子（根据类型，页码）Post
def showPost(request):
    pageSize=5
    postlist=[]
    # 有时间时再次写
    searchtype=json.loads(request.body)["navtype"]
    page=int(json.loads(request.body)["pageindex"])
    userid=json.loads(request.body)["uid"]
    postmes=list(models.Post.objects.all()[(page-1)*pageSize:page*pageSize].values("id","ptitle","ptitleimg","pdetailcont","pbriefcont"))

    for i in range(len(postmes)):
        post={}
        post["easyshow"]=True
        post["postid"]=postmes[i]["id"]
        post["posttitle"]=postmes[i]["ptitle"]
        post["postImg"]=postmes[i]["ptitleimg"]
        post["postdetailcon"]=postmes[i]["pdetailcont"]
        post["posteasycon"]=postmes[i]["pbriefcont"]
        post["postreplynum"]=models.PostReply.objects.filter(pReply_pid_id=post["postid"]).count()
        post["postcollectnum"]=models.PostCollect.objects.filter(post_id_id=post["postid"]).count()
        postcollectionstatus=models.PostCollect.objects.filter(post_id_id=post["postid"],userinfo_id=userid).count()
        if postcollectionstatus:
            post["postcollectstatus"]=True
        else:
            post["postcollectstatus"]=False
        post["postdianzannum"] = models.PostThumb.objects.filter(post_id_id=post["postid"]).count()
        postdianzanstatus=models.PostThumb.objects.filter(post_id_id=post["postid"],userinfo_id=userid).count()
        if postdianzanstatus:
            post["postdianzanstatus"]=True
        else:
            post["postdianzanstatus"] = False
        postlist.append(post)
    print(postlist)
    return JsonResponse(postlist,safe=False,json_dumps_params={"ensure_ascii":False})


#收藏帖子
def collectpost(request):
    if request.method=="POST":
        try:
            userid = json.loads(request.body)["userid"]
            postid = json.loads(request.body)["postid"]
            collectstatus = json.loads(request.body)["collectstatus"]
            if collectstatus:
                obj = models.PostCollect(userinfo_id=userid, post_id_id=postid)
                obj.save()
            else:
                models.PostCollect.objects.filter(userinfo_id=userid, post_id_id=postid).delete()
            return JsonResponse({"code":200})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":500})


#点赞帖子
def  dianzanpost(request):
    if request.method=="POST":
        # try:
        userid = json.loads(request.body)["userid"]
        postid = json.loads(request.body)["postid"]
        dianzanstatus = json.loads(request.body)["dianzanstatus"]
        if dianzanstatus:
            obj = models.PostThumb(userinfo_id=userid, post_id_id=postid)
            obj.save()
        else:
            models.PostCollect.objects.filter(userinfo_id=userid, post_id_id=postid).delete()
        return JsonResponse({"code": 200})
        # except Exception as ex:
        #     print(ex)
        #     return JsonResponse({"code": 500})




