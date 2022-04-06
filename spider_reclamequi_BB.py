from urllib.parse import urljoin
import scrapy
import logging


class ReclameaquiBbSpider(scrapy.Spider):
    name = 'reclameaqui_bb'

    
#   --- Insira o número de páginas que gostaria de raspar
    
    global complaint_url
    complaint_url =[]
    
    global pages_wanted
    pages_wanted = 3
    
    
#    allowed_domains = ['reclameaqui.com.br']
#   Cria uma lista de urls

    start_urls = [f'https://www.reclameaqui.com.br/empresa/banco-do-brasil/lista-reclamacoes/?pagina={i}&status=EVALUATED' for i in range(1, pages_wanted + 1)]
    
    def parse(self, response):
        main_url = "https://www.reclameaqui.com.br"
#   Raspa a página colhendo os href que levam às reclamações completas
        for complaint in response.xpath('//div[@class="sc-1pe7b5t-0 bJdtis"]'):
            complaint_url = (main_url + complaint.xpath('./a/@href').get())

        

#                                 ### ATENÇÃO ###
#   A linha de código numero 31 não está retornando todas as complaint_url
#   devido características do yield que ainda não consegui entender.
#   Para testar, descomente a linha abaixo e comente as linhas 33 a 35

    # def next_page(self)
    #         yield scrapy.Request(next(iter(start_urls), callback = self.get_text)
    

        
        #yield self.index_pagination
            yield {
                 'url' : complaint_url
            }

    # def index_pagination():



    def get_text(self, response):
        title = response.xpath('//div[@class="lzlu7c-19 hpNFPP"]/h1/text()').getall()
        content = response.xpath('//p[@class="lzlu7c-17 fXwQIB"]/text()').getall()
        
        
        yield {
            'title' : title,
    #        'content':content
            }

#   Resolvido o problema de não retornar todas as URLs, implementar:
#       - conteúdo da reclamação (.encode('utf-8') não está funcionando);
#       - status da reclamação;
#       - nota;

