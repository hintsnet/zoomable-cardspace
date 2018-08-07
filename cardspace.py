import json

# 定义卡片库（CardSpace）类
class CardSpace:
	# 对卡片库类的实例进行初始化
	def __init__(self, name, cards_list):
		# name 卡片库的名称
		self.name = name
		# cards_list 卡片库的初始卡片集合（含偏序关系定义）
		# 参考链接
		# https：//www.khanacademy.org/exercisedashboard
		self.cards_list = cards_list
		# 为卡片库中的卡片建立名称索引
		self.cards_dict = self.build_cards_dict(self.cards_list)
	
	# 为卡片库中的卡片集合建立索引
	def build_cards_dict(self, cards_list):
		cards_dict = {}
		inset_cards = []
		for card in cards_list:
			if card.get('name') in inset_cards:
				pass
			else:
				cards_dict[card.get('name')] = card
		return cards_dict
	
	# 给定卡片名称，获取卡片内容
	def get_card(self, name):
		return self.cards_dict.get(name)
	
	# 获取当前卡片库中所有的左边界卡片
	def get_leftedge_cards(self):
		leftedge_cards_dict = {}
		leftedge_cardnames_set = []
		for card in self.cards_list:
			if len(card.get('prereqs')) == 0:
				if card.get('name') in leftedge_cardnames_set:
					pass
				else:
					leftedge_cards_dict[card.get('name')] = card
					leftedge_cardnames_set.append(card.get('name'))
			else:
				pass
		return leftedge_cards_dict
	
	# 获取当前卡片库中所有“可扮演左项”的卡片
	def get_left_cards(self, cards_list):
		left_cards_dict = {}
		left_cardnames_set = []
		for card in cards_list:
			if len(card.get('prereqs')) > 0:
				for pre_card in card.get('prereqs'):
					if pre_card in left_cardnames_set:
						pass
					else:
						left_cards_dict[pre_card] = self.get_card(pre_card)
						left_cardnames_set.append(pre_card)
			else:
				pass
		return left_cards_dict
	
	# 获取当前卡片库中所有的右边界卡片
	def get_rightedge_cards(self):
		left_cards_dict = self.get_left_cards(self.cards_list)
		left_cardnames_set = left_cards_dict.keys()
		rightedge_cards_dict = {}
		rightedge_cardnames_set = []
		for card in cards_list:
			if card.get('name') in left_cardnames_set:
				pass
			else:
				if card.get('name') in rightedge_cardnames_set:
					pass
				else:
					rightedge_cards_dict[card.get('name')] = card
					rightedge_cardnames_set.append(card.get('name'))
		return rightedge_cards_dict


# 载入知识图 json 数据
with open('khan_kst.json', 'r', encoding='utf8') as kst_json:
	kst_json_dict = json.load(kst_json)

cards_list = kst_json_dict.get('graph_dict_data')

cardspace1 = CardSpace('数学知识图', cards_list)

print("入口知识点数目：%s " % len(cardspace1.get_leftedge_cards()))
print("出口知识点数目：%s " % len(cardspace1.get_rightedge_cards()))
