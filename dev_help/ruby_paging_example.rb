#From the Shopify docs? - MTM

# Telling your shop who's boss.
url = "https://#{APIKEY}:#{PASSWORD}@#{SHOPNAME}.myshopify.com/admin"
ShopifyAPI::Base.site = url

# How many.
product_count = ShopifyAPI::Product.count
nb_pages      = (product_count / 250.0).ceil

# Do we actually have any work to do?
puts "Yo man. You don't have any product in your shop. duh!" if product_count.zero?

# Initializing.
start_time = Time.now

# While we still have products.
1.upto(nb_pages) do |page|
  unless page == 1
    stop_time = Time.now
    puts "Last batch processing started at #{start_time.strftime('%I:%M%p')}"
    puts "The time is now #{stop_time.strftime('%I:%M%p')}"
    processing_duration = stop_time - start_time
    puts "The processing lasted #{processing_duration.to_i} seconds."
    wait_time = (CYCLE - processing_duration).ceil
    puts "We have to wait #{wait_time} seconds then we will resume."
    sleep wait_time if wait_time > 0
    start_time = Time.now
  end
  puts "Doing page #{page}/#{nb_pages}..."
  products = ShopifyAPI::Product.find( :all, :params => { :limit => 250, :page => page } )
  products.each do |product|
    puts product.title
    any_in_stock = product.variants.any? do |variant|
      variant.inventory_management == '' || variant.inventory_policy == 'continue' || variant.inventory_quantity > 0
    end
    if not any_in_stock
      puts "--- Deleting #{product.title}..."
      product.destroy
    end
  end
end

puts "Over and out."