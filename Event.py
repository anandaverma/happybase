class Event:
	   bot_ref
	   user_id
	   msg_type
	   mid
	   broadcast_id
	   msg_timestamp
	   is_delivered
	   is_read
	   platform
	   session_id
	   msg_content
	   
	def __init__(self, bot_ref, user_id, msg_type, mid, broadcast_id, msg_timestamp, is_delivered, is_read,platform, session_id, msg_content):
	      self.bot_ref = bot_ref
	      self.user_id = user_id
	      self.msg_type = msg_type
	      self.mid = mid
	      self.broadcast_id = broadcast_id
	      self.msg_timestamp = msg_timestamp
	      self.is_delivered = is_delivered
	      self.is_read = is_read
	      self.platform = platform
	      self.session_id = msg_content