from highrise.__main__ import *
import time

"""Bot Settings"""
room_id = "6692abfd94adf4bfc89fbab6"
bot_token = "03853e31cdc15928169fc555f96b7f9fbb0b6bf4aad96a721e230d203fa8a5e1"
bot_file = "main"
bot_class = "Mybot"

if __name__ == "__main__":
  definitions = [
	  BotDefinition(
	    getattr(import_module(bot_file), bot_class)(),
      room_id, 
			bot_token)]  # More BotDefinition classes can be added to the definitions list
  while True:
    try:
      arun(main(definitions))
    except Exception as e:
      # Print the full traceback for the exception
      import traceback
      print("Caught an exception:")
      traceback.print_exc()  # This will print the full traceback       
      time.sleep(1)       
      continue