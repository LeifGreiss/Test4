import scraperwiki
import lxml.html
# scrape_table function: gets passed an individual page to scrape
# where is root coming from?
def scrape_table(root):
    rows = root.cssselect("table.p.table tr")
    #rows = root.cssselect("table.Trolley.table tr")  # selects all <tr> blocks within <table class="Trolley">
    for row in rows: # where do rows come from? 
        # Set up our data record 
        record = {}
        table_cells = row.cssselect("p") #In the row use cssselect to select for td
        if table_cells: 
            record['Racecourse'] = table_cells[0].text_content
            record['Address and Phone Book'] = table_cells[1].text_content
            #record['Date'] = table_cells[0].text
            #record['Hospital'] = table_cells[1].text
            #record['Region'] = table_cells[2].text
            #record['Trolley total'] = table_cells[3].text
            #record['Ward Total'] = table_cells[4].text
            # Print out the data we've gathered
            print record, '------------'
            # Save the record to the data store with Hospital as the unique key.
            scraperwiki.sqlite.save(["Racecourse"], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
    scrape_table(root)
starting_url = 'http://www.ukjockey.com/racecourses.html'
scrape_and_look_for_next_link(starting_url)
