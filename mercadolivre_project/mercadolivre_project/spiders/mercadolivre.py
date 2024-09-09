import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/?new_categories_landing=false"]

    def parse(self, response):
        carros = response.css("li.ui-search-layout__item")
        
        for carro in carros:
            yield {
                "nome": carro.css("h2.ui-search-item__title::text").get(),
                "preco": carro.css("span.andes-money-amount__fraction::text").get(),
                
            }
