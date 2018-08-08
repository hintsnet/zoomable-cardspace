import json
import anytree

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
		leftedge_cardnames = []
		for card in self.cards_list:
			if len(card.get('prereqs')) == 0:
				if card.get('name') in leftedge_cardnames:
					pass
				else:
					leftedge_cards_dict[card.get('name')] = card
					leftedge_cardnames.append(card.get('name'))
			else:
				pass
		return leftedge_cards_dict
	
	# 获取当前卡片库中所有“可扮演左项”的卡片
	def get_left_cards(self, cards_list):
		left_cards_dict = {}
		left_cardnames = []
		for card in cards_list:
			if len(card.get('prereqs')) > 0:
				for pre_card in card.get('prereqs'):
					if pre_card in left_cardnames:
						pass
					else:
						left_cards_dict[pre_card] = self.get_card(pre_card)
						left_cardnames.append(pre_card)
			else:
				pass
		return left_cards_dict
	
	# 获取当前卡片库中所有的右边界卡片
	def get_rightedge_cards(self):
		left_cards_dict = self.get_left_cards(self.cards_list)
		left_cardnames = left_cards_dict.keys()
		rightedge_cards_dict = {}
		rightedge_cardnames = []
		for card in cards_list:
			if card.get('name') in left_cardnames:
				pass
			else:
				if card.get('name') in rightedge_cardnames:
					pass
				else:
					rightedge_cards_dict[card.get('name')] = card
					rightedge_cardnames.append(card.get('name'))
		return rightedge_cards_dict

	# 判断当前卡片是否曾被加入知识树
	def is_card_intree(cardname, ktree_root):
		intree_cards = anytree.findall(ktree_root, verify_tnode_name(cardname))
		if 0 == len(intree_cards):
			return False
		else:
			return True
			
	# 获取给定卡片的后置卡片集合
	def get_after_cards(self, cardname):
		after_cardnames_list = []
		for curr_card in self.cards_list:
			pre_cardnames = curr_card.get('prereqs')
			if cardname in pre_cardnames and \
				cardname != curr_card.get('name') and \
				cardname not in after_cardnames_list:
				after_cardnames_list.append(curr_card.get('name'))
			else:
				pass
		return after_cardnames_list
	
	# 利用卡片库中的卡片及其相互关系，生成一个树状图
	def build_knowledge_tree(self):
		# 创建一个空白的知识树，最初它只有一个入口
		ktree_inport = anytree.Node('[# 入口 #]')
		# 创建一个空白的待处理卡片队列
		todo_cards = []
		
		# 获取卡片库的左边界和右边界
		leftedge_cards_dict = self.get_leftedge_cards()
		rightedge_cards_dict = self.get_rightedge_cards()
		
		for leftedge_card_name in leftedge_cards_dict.keys():
			new_node1 = anytree.Node( \
				self.get_card(leftedge_card_name).get('display_name'), ktree_inport)
			todo_cards.append(( leftedge_card_name, new_node1 ))
		
		while(todo_cards):
			todo_card = todo_cards[0]
			todo_cards = todo_cards[1:]
			after_cardnames = self.get_after_cards(todo_card[0])
			for after_cardname in after_cardnames:
				new_node2 = anytree.Node(self.get_card(after_cardname).get('display_name'), todo_card[1])
				if after_cardname in rightedge_cards_dict.keys():
					anytree.Node('[# 出口 #]', new_node2)
				else:
					pass
				todo_cards.append(( after_cardname, new_node2 ))

		return ktree_inport

# 载入知识图 json 数据
with open('khan_kst.json', 'r', encoding='utf8') as kst_json:
	kst_json_dict = json.load(kst_json)

cards_list = kst_json_dict.get('knowledge_graph_data')

cardspace1 = CardSpace('数学知识图', cards_list)

ktree_root = cardspace1.build_knowledge_tree()

print(anytree.RenderTree(ktree_root, style=anytree.AsciiStyle()).by_attr())
