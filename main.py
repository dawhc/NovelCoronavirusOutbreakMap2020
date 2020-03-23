# -!- coding: utf-8 -!-
import web
import time
import json
import requests
import os
from pyecharts import options as opts
from pyecharts.charts import *

DIR_NAME = os.path.dirname(__file__)
nameMap = {'新加坡': 'Singapore Rep.', '多米尼加': 'Dominican Rep.', '巴勒斯坦': 'Palestine', '巴哈马': 'The Bahamas', '东帝汶': 'East Timor', '阿富汗': 'Afghanistan', '几内亚比绍': 'Guinea Bissau', '科特迪瓦': "Côte d'Ivoire", '锡亚琴冰川': 'Siachen Glacier', '英属印度洋领土': 'Br. Indian Ocean Ter.', '安哥拉': 'Angola', '阿尔巴尼亚': 'Albania', '阿联酋': 'United Arab Emirates', '阿根廷': 'Argentina', '亚美尼亚': 'Armenia', '法属南半球和南极领地': 'French Southern and Antarctic Lands', '澳大利亚': 'Australia', '奥地利': 'Austria', '阿塞拜疆': 'Azerbaijan', '布隆迪': 'Burundi', '比利时': 'Belgium', '贝宁': 'Benin', '布基纳法索': 'Burkina Faso', '孟加拉国': 'Bangladesh', '保加利亚': 'Bulgaria', '波斯尼亚和黑塞哥维那': 'Bosnia and Herz.', '白俄罗斯': 'Belarus', '伯利兹': 'Belize', '百慕大': 'Bermuda', '玻利维亚': 'Bolivia', '巴西': 'Brazil', '文莱': 'Brunei', '不丹': 'Bhutan', '博茨瓦纳': 'Botswana', '中非': 'Central African Rep.', '加拿大': 'Canada', '瑞士': 'Switzerland', '智利': 'Chile', '中国': 'China', '象牙海岸': 'Ivory Coast', '喀麦隆': 'Cameroon', '刚果民主共和国': 'Dem. Rep. Congo', '刚果': 'Congo', '哥伦比亚': 'Colombia', '哥斯达黎加': 'Costa Rica', '古巴': 'Cuba', '北塞浦路斯': 'N. Cyprus', '塞浦路斯': 'Cyprus', '捷克': 'Czech Rep.', '德国': 'Germany', '吉布提': 'Djibouti', '丹麦': 'Denmark', '阿尔及利亚': 'Algeria', '厄瓜多尔': 'Ecuador', '埃及': 'Egypt', '厄立特里亚': 'Eritrea', '西班牙': 'Spain', '爱沙尼亚': 'Estonia', '埃塞俄比亚': 'Ethiopia', '芬兰': 'Finland', '斐': 'Fiji', '福克兰群岛': 'Falkland Islands', '法国': 'France', '加蓬': 'Gabon', '英国': 'United Kingdom', '格鲁吉亚': 'Georgia', '加纳': 'Ghana', '几内亚': 'Guinea', '冈比亚': 'Gambia', '赤道几内亚': 'Eq. Guinea', '希腊': 'Greece', '格陵兰': 'Greenland', '危地马拉': 'Guatemala', '法属圭亚那': 'French Guiana', '圭亚那': 'Guyana', '洪都拉斯': 'Honduras', '克罗地亚': 'Croatia', '海地': 'Haiti', '匈牙利': 'Hungary', '印度尼西亚': 'Indonesia', '印度': 'India', '爱尔兰': 'Ireland', '伊朗': 'Iran', '伊拉克': 'Iraq', '冰岛': 'Iceland', '以色列': 'Israel', '意大利': 'Italy', '牙买加': 'Jamaica', '约旦': 'Jordan', '日本本土': 'Japan', '哈萨克斯坦': 'Kazakhstan', '肯尼亚': 'Kenya', '吉尔吉斯斯坦': 'Kyrgyzstan', '柬埔寨': 'Cambodia', '韩国': 'Korea', '科索沃': 'Kosovo', '科威特': 'Kuwait', '老挝': 'Lao PDR', '黎巴嫩': 'Lebanon', '利比里亚': 'Liberia', '利比亚': 'Libya', '斯里兰卡': 'Sri Lanka', '莱索托': 'Lesotho', '立陶宛': 'Lithuania', '卢森堡': 'Luxembourg', '拉脱维亚': 'Latvia', '摩洛哥': 'Morocco', '摩尔多瓦': 'Moldova', '马达加斯加': 'Madagascar', '墨西哥': 'Mexico', '马其顿': 'Macedonia', '马里': 'Mali', '缅甸': 'Myanmar', '黑山': 'Montenegro', '蒙古': 'Mongolia', '莫桑比克': 'Mozambique', '毛里塔尼亚': 'Mauritania', '马拉维': 'Malawi', '马来西亚': 'Malaysia', '纳米比亚': 'Namibia', '新喀里多尼亚': 'New Caledonia', '尼日尔': 'Niger', '尼日利亚': 'Nigeria', '尼加拉瓜': 'Nicaragua', '荷兰': 'Netherlands', '挪威': 'Norway', '尼泊尔': 'Nepal', '新西兰': 'New Zealand', '阿曼': 'Oman', '巴基斯坦': 'Pakistan', '巴拿马': 'Panama', '秘鲁': 'Peru', '菲律宾': 'Philippines', '巴布亚新几内亚': 'Papua New Guinea', '波兰': 'Poland', '波多黎各': 'Puerto Rico', '朝鲜': 'Dem. Rep. Korea', '葡萄牙': 'Portugal', '巴拉圭': 'Paraguay', '卡塔尔': 'Qatar', '罗马尼亚': 'Romania', '俄罗斯': 'Russia', '卢旺达': 'Rwanda', '西撒哈拉': 'W. Sahara', '沙特阿拉伯': 'Saudi Arabia', '苏丹': 'Sudan', '南苏丹': 'S. Sudan', '塞内加尔': 'Senegal', '所罗门群岛': 'Solomon Is.', '塞拉利昂': 'Sierra Leone', '萨尔瓦多': 'El Salvador', '索马里兰': 'Somaliland', '索马里': 'Somalia', '塞尔维亚': 'Serbia', '苏里南': 'Suriname', '斯洛伐克': 'Slovakia', '斯洛文尼亚': 'Slovenia', '瑞典': 'Sweden', '斯威士兰': 'Swaziland', '叙利亚': 'Syria', '乍得': 'Chad', '多哥': 'Togo', '泰国': 'Thailand', '塔吉克斯坦': 'Tajikistan', '土库曼斯坦': 'Turkmenistan', '特里尼达和多巴哥': 'Trinidad and Tobago', '突尼斯': 'Tunisia', '土耳其': 'Turkey', '坦桑尼亚': 'Tanzania', '乌干达': 'Uganda', '乌克兰': 'Ukraine', '乌拉圭': 'Uruguay', '美国': 'United States', '乌兹别克斯坦': 'Uzbekistan', '委内瑞拉': 'Venezuela', '越南': 'Vietnam', '瓦努阿图': 'Vanuatu', '西岸': 'West Bank', '也门': 'Yemen', '南非': 'South Africa', '赞比亚': 'Zambia', '津巴布韦': 'Zimbabwe'}
cnCity = {'安徽': {'合肥': '340100', '芜湖': '340200', '蚌埠': '340300', '淮南': '340400', '马鞍': '340500', '淮北': '340600', '铜陵': '340700', '安庆': '340800', '黄山': '341000', '滁州': '341100', '阜阳': '341200', '宿州': '341300', '六安': '341500', '亳州': '341600', '池州': '341700', '宣城': '341800'}, '福建': {'福州': '350100', '厦门': '350200', '莆田': '350300', '三明': '350400', '泉州': '350500', '漳州': '350600', '南平': '350700', '龙岩': '350800', '宁德': '350900'}, '广东': {'广州': '440100', '韶关': '440200', '深圳': '440300', '珠海': '440400', '汕头': '440500', '佛山': '440600', '江门': '440700', '湛江': '440800', '茂名': '440900', '肇庆': '441200', '惠州': '441300', '梅州': '441400', '汕尾': '441500', '河源': '441600', '阳江': '441700', '清远': '441800', '东莞': '441900', '中山': '442000', '潮州': '445100', '揭阳': '445200', '云浮': '445300'}, '广西': {'南宁': '450100', '柳州': '450200', '桂林': '450300', '梧州': '450400', '北海': '450500', '防城': '450600', '钦州': '450700', '贵港': '450800', '玉林': '450900', '百色': '451000', '贺州': '451100', '河池': '451200', '来宾': '451300', '崇左': '451400'}, '贵州': {'贵阳': '520100', '六盘': '520200', '遵义': '520300', '安顺': '520400', '毕节': '520500', '铜仁': '520600', '黔西': '522300', '黔东': '522600', '黔南': '522700'}, '甘肃': {'兰州': '620100', '嘉峪': '620200', '金昌': '620300', '白银': '620400', '天水': '620500', '武威': '620600', '张掖': '620700', '平凉': '620800', '酒泉': '620900', '庆阳': '621000', '定西': '621100', '陇南': '621200', '临夏': '622900', '甘南': '623000'}, '河北': {'石家': '130100', '唐山': '130200', '秦皇': '130300', '邯郸': '130400', '邢台': '130500', '保定': '130600', '张家': '130700', '承德': '130800', '沧州': '130900', '廊坊': '131000', '衡水': '131100'}, '黑龙江': {'哈尔': '230100', '齐齐': '230200', '鸡西': '230300', '鹤岗': '230400', '双鸭': '230500', '大庆': '230600', '伊春': '230700', '佳木': '230800', '七台': '230900', '牡丹': '231000', '黑河': '231100', '绥化': '231200', '大兴': '232700'}, '河南': {'郑州': '410100', '开封': '410200', '洛阳': '410300', '平顶': '410400', '安阳': '410500', '鹤壁': '410600', '新乡': '410700', '焦作': '410800', '濮阳': '410900', '许昌': '411000', '漯河': '411100', '三门': '411200', '南阳': '411300', '商丘': '411400', '信阳': '411500', '周口': '411600', '驻马': '411700', '济源': '419001'}, '湖北': {'武汉': '420100', '黄石': '420200', '十堰': '420300', '宜昌': '420500', '襄阳': '420600', '鄂州': '420700', '荆门': '420800', '孝感': '420900', '荆州': '421000', '黄冈': '421100', '咸宁': '421200', '随州': '421300', '恩施': '422800', '仙桃': '429004', '潜江': '429005', '天门': '429006', '神农': '429021'}, '湖南': {'长沙': '430100', '株洲': '430200', '湘潭': '430300', '衡阳': '430400', '邵阳': '430500', '岳阳': '430600', '常德': '430700', '张家': '430800', '益阳': '430900', '郴州': '431000', '永州': '431100', '怀化': '431200', '娄底': '431300', '湘西': '433100'}, '海南': {'海口': '460100', '三亚': '460200', '三沙': '460300', '儋州': '460400'}, '吉林': {'长春': '220100', '吉林': '220200', '四平': '220300', '辽源': '220400', '通化': '220500', '白山': '220600', '松原': '220700', '白城': '220800', '延边': '222400'}, '江苏': {'南京': '320100', '无锡': '320200', '徐州': '320300', '常州': '320400', '苏州': '320500', '南通': '320600', '连云': '320700', '淮安': '320800', '盐城': '320900', '扬州': '321000', '镇江': '321100', '泰州': '321200', '宿迁': '321300'}, '江西': {'南昌': '360100', '景德': '360200', '萍乡': '360300', '九江': '360400', '新余': '360500', '鹰潭': '360600', '赣州': '360700', '吉安': '360800', '宜春': '360900', '抚州': '361000', '上饶': '361100'}, '辽宁': {'沈阳': '210100', '大连': '210200', '鞍山': '210300', '抚顺': '210400', '本溪': '210500', '丹东': '210600', '锦州': '210700', '营口': '210800', '阜新': '210900', '辽阳': '211000', '盘锦': '211100', '铁岭': '211200', '朝阳': '211300', '葫芦': '211400'}, '内蒙古': {'呼和': '150100', '包头': '150200', '乌海': '150300', '赤峰': '150400', '通辽': '150500', '鄂尔': '150600', '呼伦': '150700', '巴彦': '150800', '乌兰': '150900', '兴安': '152200', '锡林': '152500', '阿拉': '152900'}, '宁夏': {'银川': '640100', '石嘴': '640200', '吴忠': '640300', '固原': '640400', '中卫': '640500'}, '青海': {'西宁': '630100', '海东': '630200', '海北': '632200', '黄南': '632300', '海南': '632500', '果洛': '632600', '玉树': '632700', '海西': '632800'}, '山西': {'太原': '140100', '大同': '140200', '阳泉': '140300', '长治': '140400', '晋城': '140500', '朔州': '140600', '晋中': '140700', '运城': '140800', '忻州': '140900', '临汾': '141000', '吕梁': '141100'}, '山东': {'济南': '370100', '青岛': '370200', '淄博': '370300', '枣庄': '370400', '东营': '370500', '烟台': '370600', '潍坊': '370700', '济宁': '370800', '泰安': '370900', '威海': '371000', '日照': '371100', '莱芜': '371200', '临沂': '371300', '德州': '371400', '聊城': '371500', '滨州': '371600', '菏泽': '371700'}, '四川': {'成都': '510100', '自贡': '510300', '攀枝': '510400', '泸州': '510500', '德阳': '510600', '绵阳': '510700', '广元': '510800', '遂宁': '510900', '内江': '511000', '乐山': '511100', '南充': '511300', '眉山': '511400', '宜宾': '511500', '广安': '511600', '达州': '511700', '雅安': '511800', '巴中': '511900', '资阳': '512000', '阿坝': '513200', '甘孜': '513300', '凉山': '513400'}, '陕西': {'西安': '610100', '铜川': '610200', '宝鸡': '610300', '咸阳': '610400', '渭南': '610500', '延安': '610600', '汉中': '610700', '榆林': '610800', '安康': '610900', '商洛': '611000'}, '天津': {'天津': '120100'}, '台湾': {'台北': '719002', '高雄': '719019', '台中': '719017', '台南': '719016', '新北': '719010', '基隆': '719011', '新竹': '719006', '嘉义': '719004'}, '西藏': {'拉萨': '540100', '日喀': '540200', '昌都': '540300', '林芝': '540400', '山南': '540500', '那曲': '540600', '阿里': '542500'}, '新疆': {'乌鲁': '650100', '克拉': '650200', '吐鲁': '650400', '哈密': '650500', '昌吉': '652300', '博尔': '652700', '巴音': '652800', '阿克': '652900', '克孜': '653000', '喀什': '653100', '和田': '653200', '伊犁': '654000', '塔城': '654200', '阿勒': '654300', '石河': '659001', '阿拉': '659002', '图木': '659003', '五家': '659004'}, '云南': {'昆明': '530100', '曲靖': '530300', '玉溪': '530400', '保山': '530500', '昭通': '530600', '丽江': '530700', '普洱': '530800', '临沧': '530900', '楚雄': '532300', '红河': '532500', '文山': '532600', '西双': '532800', '大理': '532900', '德宏': '533100', '怒江': '533300', '迪庆': '533400'}, '浙江': {'杭州': '330100', '宁波': '330200', '温州': '330300', '嘉兴': '330400', '湖州': '330500', '绍兴': '330600', '金华': '330700', '衢州': '330800', '舟山': '330900', '台州': '331000', '丽水': '331100'}}

class DataHandler(object):

    def __init__(self):
        self.data = [1]
        self.url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)

    @staticmethod
    def get_fullname(prov, city):
        if prov in ['北京', '上海', '天津', '重庆']:
            return city + ('' if city[-1] == '区' else '区')
        try:
            url = 'https://geo.datav.aliyun.com/areas/bound/' + cnCity[prov][city[:2]] + '.json'
            return requests.get(url).json()['features'][0]['properties']['name']
        except:
            return city

    def get_data(self):
        self.data = json.loads(requests.get(url=self.url).json()['data'])
        return self.data

    def render_static(self):

        data = self.data['areaTree'][0]['children']
        cn_data = []

        for char in data:
            cn_data.append([char['name'], char['total']['confirm']])


        cn_map = Map(init_opts=opts.InitOpts(width='1350px', height='750px'))
        cn_map.add("", cn_data, "china", is_map_symbol_show=False)
        cn_map.set_global_opts(title_opts=opts.TitleOpts(title="国内疫情地图" + '（更新时间：' + self.data['lastUpdateTime'] + '）'),
                                visualmap_opts=opts.VisualMapOpts(max_=3000, is_piecewise=True,
                                pieces=[
                                    {"min": "0", "max": "10", "label": "0-10", "color": "#FFA07A"},
                                    {"min": "10", "max": "100", "label": "10-100", "color": "#FF7F50"},
                                    {"min": "100", "max": "1000", "label": "100-1000", "color": "#FF4500"},
                                    {"min": "1000", "max": "10000", "label": "1000-10000", "color": "#FF0000"},
                                    {"min": "10000", "max": "5000000", "label": ">10000", "color": "#B22222"},
                                ]))
        cn_map.render(os.path.join(DIR_NAME, "statics/map_cn.html"))

        data = self.data['areaTree']
        world_data = []
        for char in data:
            try:
                world_data.append([nameMap[char['name']], char['total']['confirm']])
            except KeyError:
                pass

        world_map = Map(init_opts=opts.InitOpts(width='1350px', height='750px'))
        world_map.add("", world_data, "world", is_map_symbol_show=False)
        world_map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        world_map.set_global_opts(title_opts=opts.TitleOpts(title="世界疫情地图" + '（更新时间：' + self.data['lastUpdateTime'] + '）'),
                                visualmap_opts=opts.VisualMapOpts(max_=3000, is_piecewise=True,
                                pieces=[
                                    {"min": "0", "max": "10", "label": "0-10", "color": "#FFA07A"},
                                    {"min": "10", "max": "100", "label": "10-100", "color": "#FF7F50"},
                                    {"min": "100", "max": "1000", "label": "100-1000", "color": "#FF4500"},
                                    {"min": "1000", "max": "10000", "label": "1000-10000", "color": "#FF0000"},
                                    {"min": "10000", "max": "5000000", "label": ">10000", "color": "#B22222"},
                                ]))

        world_map.render(os.path.join(DIR_NAME, 'statics/map_world.html'))



    def render_query(self, q):


        cities = []
        total = []
        today = []
        heal = []
        dead = []
        city_data = []
        data = self.data['areaTree'][0]['children']
        for p in data:
            if p['name'] != q:
                continue
            for city in p['children']:
                city_data.append([DataHandler.get_fullname(q, city['name']), city['total']['confirm']])
                cities.append(city['name'])
                today.append(city['today']['confirm'])
                total.append(city['total']['confirm'])
                heal.append(city['total']['heal'])
                dead.append(city['total']['dead'])
            break


        print()
        bar = Bar(init_opts=opts.InitOpts(width='1350px', height='750px')) \
            .add_xaxis(cities) \
            .add_yaxis('确诊', total,) \
            .add_yaxis('新增', today,) \
            .add_yaxis('治愈', heal,) \
            .add_yaxis('死亡', dead,) \
            .reversal_axis() \
            .set_series_opts(label_opts=opts.LabelOpts(position="right")) \
            .set_global_opts(title_opts=opts.TitleOpts(title=q + '省（市）疫情柱状图'))
            


        bar.render(os.path.join(DIR_NAME, 'statics/query_bar.html'))

        map = Map(init_opts=opts.InitOpts(width='1350px', height='750px'))
        map.add("", city_data, q, is_map_symbol_show=False)
        map.set_global_opts(
            title_opts=opts.TitleOpts(title=q + "省（市）疫情地图"),
            visualmap_opts=opts.VisualMapOpts(max_=3000, is_piecewise=True,
                                              pieces=[
                                                  {"min": "0", "max": "10", "label": "0-10", "color": "#FFA07A"},
                                                  {"min": "10", "max": "100", "label": "10-100", "color": "#FF7F50"},
                                                  {"min": "100", "max": "1000", "label": "100-1000", "color": "#FF4500"},
                                                  {"min": "1000", "max": "10000", "label": "1000-10000", "color": "#FF0000"},
                                                  {"min": "10000", "max": "5000000", "label": ">10000", "color": "#B22222"},
                                              ]))
        map.render(os.path.join(DIR_NAME, 'statics/query_map.html'))


    def update(self):
        self.get_data()
        self.render_static()

dh = DataHandler()
dh.update()

urls = (
    '/', 'Index',
    '/query/(.*)', 'Query',
    '/sync', 'Sync',
    '/world', 'WorldMap',
    '/china', 'ChinaMap',
    '/result/(.*)', 'QResult',
)

class WorldMap:
    def GET(self):
        return render.map_world()

class ChinaMap:
    def GET(self):
        return render.map_cn()

class QResult:
    def GET(self, params):
        if params == 'bar':
            return render.query_bar()
        else:
            return render.query_map()

class Index:
    def GET(self):
        return render.index()

class Query:
    def GET(self, params):
        dh.render_query(params)
        return render.query(params + '查询结果')

class Sync:
    def GET(self):
        dh.update()
        return json.dumps({'code': 1})


render = web.template.render(os.path.join(DIR_NAME, 'statics/'))
app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()

