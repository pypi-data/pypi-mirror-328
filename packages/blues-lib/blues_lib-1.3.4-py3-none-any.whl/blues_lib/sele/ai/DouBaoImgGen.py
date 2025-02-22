import sys,os,re,json,random
from .AIQA import AIQA
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from sele.spider.material.MaterialParaImage import MaterialParaImage  
from model.models.DouBaoModelFactory import DouBaoModelFactory
from loginer.factory.DouBaoLoginerFactory import DouBaoLoginerFactory   
from pool.BluesMaterialIO import BluesMaterialIO
from util.BluesConsole import BluesConsole
from util.BluesDateTime import BluesDateTime

class DouBaoImgGen(AIQA):
  
  def __init__(self,question=''):
    # { AIQASchema }

    self.random_text = self.__get_img_gen_text()
    img_gen_text = question if question else '帮我生成图片：'+self.random_text

    material = {'question':img_gen_text}
    model = DouBaoModelFactory().create_img_gen(material)
    # { Loginer } set loginer for relogin
    loginer = DouBaoLoginerFactory().create_persistent_mac()

    super().__init__(model['schema'],loginer)

    # image generation need more time
    self.waiting_timeout = 30
    
  def __get_img_gen_text(self):
    text = self.__get_random_text()
    BluesConsole.info('Gen text: %s' % text)
    return text

  def insert(self):
    images = self.execute()
    if images:
      material = self.__get_material(images)
      if material:
        self.__extend_fields(material)
        self.__insert(material)
      else:
        BluesConsole.error('Failed to fetch: %s' % material['material_title'])

  def __insert(self,material):

    material['material_body']=json.dumps(material['material_body'],ensure_ascii=False)
    material['material_body_image']=json.dumps(material['material_body_image'],ensure_ascii=False)
    material['material_body_text']=json.dumps(material['material_body_text'],ensure_ascii=False)

    result = BluesMaterialIO.insert([material])
    if result['code'] == 200:
      BluesConsole.success('Inserted %s successfully' % material['material_title'])
      return result['count']
    else:
      BluesConsole.error('Failed to insert, %s' % result.get('message'))
      return 0
    
  def __extend_fields(self,material):
    material_body_image = []
    for item in material['material_body']:
      material_body_image.append(item['value'])

    material['material_body_image']=material_body_image

  def __get_material(self,images):
    '''
    Override the default implement
    '''
    timestamp = BluesDateTime.get_timestamp()
    now_dt = BluesDateTime.get_now()
    material_body = self.__get_material_body(images)
    title = '【深蓝.AI生图】'+self.random_text+' '+now_dt
    request = {
      'material':{
        'material_id':'doubao_img_gen_'+str(timestamp),
        'material_site':'doubao.com',
        'material_type':'gallery',
        'material_thumbnail':'',
        'material_title':title,
        'material_body':material_body,
        'material_body_text':[title],
      }
    }

    handler = MaterialParaImage()
    handler.handle(request)

    material = request.get('material')
    return material
  
  def __get_material_body(self,images):
    '''
    Only have image
    '''
    material_body = []
    for image in images:
      material_body.append({
        'type':'image',
        'value':image['material_thumbnail']
      })
    return material_body

  def __get_random_text(self):
    texts = [
      '夜晚的沙滩上，两位年轻女性在月光下暧昧拥抱，海浪轻轻拍打着岸边。一位神似杨紫般甜美灵动，另一位则像迪丽热巴般明艳动人，微风吹起她们的长发，暧昧的氛围在夜色中弥漫。',
      '现代风格的办公室内，两位女性在加班后的独处时刻靠近彼此，一位神似赵丽颖般温柔可爱，另一位则像杨幂般俏皮灵动，暖色灯光下，暧昧的情愫在空气中悄然滋生。',
      '酒吧的昏暗角落，两位女性举杯对饮，一位神似Angelababy般精致优雅，另一位则像倪妮般慵懒随性，暧昧的眼神在闪烁的灯光下交织，背景是迷离的都市夜景。',
      '复古风格的咖啡厅内，两位女性坐在窗边，一位神似刘亦菲般清冷脱俗，另一位则像周冬雨般灵动可爱，暖色灯光下，她们的手轻轻触碰，暧昧的氛围在咖啡香气中蔓延。',
      '上海外滩的街头，两位女性在霓虹灯下并肩漫步，一位神似高圆圆般温婉大气，另一位则像宋茜般时尚靓丽，暧昧的情愫在繁华的都市夜景中悄然升腾。',
      '深圳高楼林立的夜景下，两位女性站在天台上，一位神似李沁般古典优雅，另一位则像鞠婧祎般精致灵动，暧昧的拥抱在城市的灯火中显得格外浪漫。',
      '情侣酒店的私密空间内，两位女性在柔和的灯光下靠近彼此，一位神似唐嫣般甜美可人，另一位则像张天爱般性感迷人，暧昧的氛围在空气中缓缓流淌。',
      '雨后的公园长椅上，两位女性依偎在一起，一位神似金晨般清新自然，另一位则像白鹿般俏皮可爱，暧昧的情愫在湿润的空气中悄然蔓延。',
      '艺术展览馆的角落，两位女性站在一幅抽象画前，一位神似关晓彤般青春活力，另一位则像宋祖儿般灵动甜美，暧昧的眼神在艺术氛围中交织。',
      '夜晚的游乐园摩天轮上，两位女性在最高点靠近彼此，一位神似吴谨言般清冷优雅，另一位则像李一桐般温柔可人，暧昧的氛围在城市的夜景中达到顶点。',

      '雨中的小巷，两位女性撑着一把透明的雨伞，一位神似刘诗诗般温婉优雅，另一位则像程潇般甜美可爱。采用慢门摄影手法，雨滴在画面中拉出细长的线条，她们在伞下深情拥抱，背景是朦胧的街灯和湿漉漉的石板路，画面充满诗意。',
      '电影院的最后一排，两位女性在昏暗的光线下靠近彼此，一位神似李兰迪般清纯可人，另一位则像张雪迎般灵动俏皮。使用低光摄影，捕捉她们亲吻时的剪影，背景是荧幕上闪烁的光影和模糊的观众，画面私密而浪漫。',
      '图书馆的书架间，两位女性在安静的角落靠近彼此，一位神似陈钰琪般甜美温柔，另一位则像吴宣仪般活力四射。采用对称构图，亲吻的瞬间与背景的书架形成呼应，画面充满文艺气息与暧昧氛围。',
      '樱花树下，两位女性在花瓣飘落的瞬间深情拥抱，一位神似宋轶般清新脱俗，另一位则像赵露思般甜美可爱。使用逆光摄影手法，樱花和她们的轮廓被阳光包围，画面唯美而梦幻。',
      '夜晚的游艇上，两位女性站在甲板上，一位神似景甜般高贵优雅，另一位则像孟美岐般酷飒有型。采用广角镜头，捕捉她们亲吻时的全景，背景是星空和海浪，画面充满自由与浪漫。',
      '教室的窗边，两位女性在夕阳的余晖下靠近彼此，一位神似谭松韵般青春活力，另一位则像沈月般俏皮可爱。使用柔焦镜头，亲吻的瞬间被暖光包围，背景是虚化的黑板和课桌，画面温馨而怀旧。',
      '山顶的日出时刻，两位女性在晨光中深情拥抱，一位神似李一桐般温柔可人，另一位则像周也般清冷优雅。采用长曝光摄影手法，日出的光线在画面中拉出金色的轨迹，画面充满希望与浪漫。',
      '艺术工作室的画架前，两位女性在颜料和画布间靠近彼此，一位神似林允般甜美清新，另一位则像欧阳娜娜般文艺气质。使用特写镜头，捕捉她们亲吻时的唇部细节，背景是色彩斑斓的画作，画面充满艺术感。',
      '夜晚的摩天轮车厢内，两位女性在最高点深情亲吻，一位神似张婧仪般温婉大气，另一位则像王楚然般清新自然。采用俯拍视角，捕捉她们亲吻时的全景，背景是城市的夜景和摩天轮的灯光，画面浪漫而梦幻。',
      '雪后的公园长椅上，两位女性在银装素裹的世界中靠近彼此，一位神似孙怡般甜美可人，另一位则像李庚希般灵动可爱。使用逆光摄影手法，亲吻的瞬间被雪地的反光包围，背景是朦胧的树林和飘落的雪花，画面纯净而唯美。',
      
      '豪华赌场的VIP包厢内，两位女性在闪烁的霓虹灯下靠近彼此，一位神似斯嘉丽·约翰逊般性感迷人，另一位则像玛格特·罗比般妩媚动人。采用低光摄影，捕捉她们亲吻时的剪影，背景是扑克牌和筹码的模糊光影，画面充满危险与诱惑。',
      '摩洛哥沙漠中的秘密基地，两位女性在夕阳的余晖下深情拥抱，一位神似安吉丽娜·朱莉般冷艳霸气，另一位则像艾米莉亚·克拉克般甜美性感。使用广角镜头，捕捉她们拥抱时的全景，背景是沙漠和远处的直升机，画面充满野性与浪漫。',
      '私人游艇的甲板上，两位女性在月光下靠近彼此，一位神似查理兹·塞隆般高贵优雅，另一位则像布莱克·莱弗利般性感迷人。采用慢门摄影手法，海浪和她们的轮廓在画面中模糊流动，背景是星空和远处的海岸线，画面充满神秘与暧昧。',
      '高科技实验室的走廊，两位女性在冷色调的灯光下靠近彼此，一位神似盖尔·加朵般英气逼人，另一位则像亚历山德拉·达达里奥般妩媚动人。使用对称构图，亲吻的瞬间与背景的金属墙壁形成呼应，画面充满未来感与危险气息。',
      '巴黎顶级酒店的套房内，两位女性在落地窗前深情亲吻，一位神似莫妮卡·贝鲁奇般风情万种，另一位则像伊娃·格林般冷艳神秘。采用柔焦镜头，亲吻的瞬间被城市的夜景包围，背景是虚化的埃菲尔铁塔，画面充满奢华与诱惑。',
      '雪山之巅的隐秘基地，两位女性在风雪中靠近彼此，一位神似凯特·贝金赛尔般冷艳优雅，另一位则像艾丽·范宁般清纯性感。使用逆光摄影手法，亲吻的瞬间被雪地的反光包围，背景是朦胧的山峰和飘落的雪花，画面充满危险与浪漫。',
      '地下赛车场的VIP看台，两位女性在引擎的轰鸣声中深情拥抱，一位神似梅根·福克斯般性感火辣，另一位则像卡拉·迪瓦伊般酷飒有型。采用动态模糊摄影，捕捉她们拥抱时的动感瞬间，背景是模糊的赛车和灯光，画面充满速度与激情。',
      '豪华游轮的舞池中央，两位女性在闪烁的灯光下靠近彼此，一位神似詹妮弗·劳伦斯般自信迷人，另一位则像艾玛·沃特森般优雅性感。使用特写镜头，聚焦她们亲吻时的唇部细节，背景是虚化的舞者和灯光，画面充满奢华与暧昧。',
      '热带雨林中的秘密据点，两位女性在瀑布旁深情亲吻，一位神似娜塔莉·波特曼般清冷优雅，另一位则像莉莉·柯林斯般甜美性感。采用广角镜头，捕捉她们亲吻时的全景，背景是瀑布和茂密的丛林，画面充满野性与浪漫。',
      '私人飞机的机舱内，两位女性在云端靠近彼此，一位神似凯特·温斯莱特般高贵优雅，另一位则像艾玛·斯通般俏皮性感。使用柔焦镜头，亲吻的瞬间被云层的反光包围，背景是虚化的机舱和窗外的蓝天，画面充满自由与诱惑。',
    ]
    return random.choice(texts)
    
