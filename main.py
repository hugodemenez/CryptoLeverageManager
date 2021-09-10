import Python_Brokers_API
import time,datetime,os











class tracker:
    
    def __init__(self):
        self.leveraged_token = 'EOSBULL'
        self.broker = Python_Brokers_API.ftx()
        self.broker.connect_key("ftx.key")
        self.initial_usd_value = self.broker.get_balances(self.leveraged_token)['usdValue']
        self.daily_usd_value = self.initial_usd_value
        self.hourly_usd_value = self.initial_usd_value
        
        while(True):
            try:
                os.system('cls' if os.name=='nt' else 'clear')
                self.tracking()
                time.sleep(5)
            except Exception as error:
                if  error == KeyboardInterrupt:
                    break
                
                print(error)
                
                
    def tracking(self):
        usd_value = self.broker.get_balances(self.leveraged_token)['usdValue']
        if datetime.datetime.now().hour == 0:
            #Si la variation journalière est négative alors on augmente la position
            if round((self.current_usd_value/self.daily_usd_value-1)*100,2) < 0:
                self.broker.create_market_order(self.leveraged_token,"buy",)
            self.daily_usd_value = usd_value
            
        if datetime.datetime.now().minute == 0:
            self.hourly_usd_value = usd_value
            
        self.current_usd_value = usd_value
        
        
        print(f"""
Le solde actuel est de : {round(self.current_usd_value,2)} $

La variation journalière est de {round((self.current_usd_value/self.daily_usd_value-1)*100,2)} %

La variation horaire est de {round((self.current_usd_value/self.hourly_usd_value-1)*100,2)} %

La variation depuis le démarrage du tracker est de {round((self.current_usd_value/self.initial_usd_value-1)*100,2)} %
"""
              )
        
            





if __name__ == '__main__':
    tracker()