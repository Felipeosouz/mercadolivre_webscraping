import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    # start_urls = ["https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/?new_categories_landing=false"]
    start_urls = ["https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes-em-bahia/?new_categories_landing=false#applied_filter_id%3Dstate%26applied_filter_name%3DLocalização%26applied_filter_order%3D6%26applied_value_id%3DTUxCUEJBSEFlYmEx%26applied_value_name%3DBahia%26applied_value_order%3D1%26applied_value_results%3D9901%26is_custom%3Dfalse"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        carros = response.css("li.ui-search-layout__item")
        
        for carro in carros:

            carro_info = carro.css('ul.ui-search-card-attributes li.ui-search-card-attributes__attribute::text').getall()

            carro_year = carro_info[0] if len(carro_info) > 0 else 'N/A'
            carro_km = carro_info[1] if len(carro_info) > 1 else 'N/A'


            yield {
                "nome": carro.css("h2.ui-search-item__title::text").get(),
                "preco": carro.css("span.andes-money-amount__fraction::text").get(),
                "ano": carro_year,
                "km": carro_km,
                "historico/vistoria": carro.css("span.ui-pb-label::text").get(),
                "vendedor": carro.css("p.ui-search-official-store-label.ui-search-item__group__element.ui-search-color--GRAY::text").get(),
                "localização": carro.css("span.ui-search-item__group__element.ui-search-item__location::text").get()
            }

        if self.page_count < self.max_pages:
            next_page = response.css("li.andes-pagination__button.andes-pagination__button--next a::attr(href)").get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
