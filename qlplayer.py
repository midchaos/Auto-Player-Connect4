class QLearnedPlayer(Player):

	def __init__(self, coin_type, epsilon=0.2, alpha=0.3, gamma=0.9):
        
		Player.__init__(self, coin_type)
		self.q = {}
		self.epsilon = epsilon 
		self.alpha = alpha 
		self.gamma = gamma 

	def getQ(self, state, action):
     
		if self.q.get((state, action)) is None:
		    self.q[(state, action)] = 1.0
		return self.q.get((state, action))

	def choose_action(self, state, actions):
        
		current_state = state

		if random.random() < self.epsilon: 
		    chosen_action = random.choice(actions)
		    return chosen_action

		qs = [self.getQ(current_state, a) for a in actions]
		maxQ = max(qs)

		if qs.count(maxQ) > 1:
		    # more than 1 best option; choose among them randomly
		    best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
		    i = random.choice(best_options)
		else:
		    i = qs.index(maxQ)

		return actions[i]

	def learn(self, board, actions, chosen_action, game_over, game_logic):
		
		reward = 0
		if (game_over):
		    win_value = game_logic.get_winner()
		    if win_value == 0:
		        reward = 0.5
		    elif win_value == self.coin_type:
		        reward = 1
		    else:
		        reward = -2
		prev_state = board.get_prev_state()
		prev = self.getQ(prev_state, chosen_action)
		result_state = board.get_state()
		maxqnew = max([self.getQ(result_state, a) for a in actions])
		self.q[(prev_state, chosen_action)] = prev + self.alpha * ((reward + self.gamma*maxqnew) - prev)
