string newProduct =
            "{" +
                "\"product\": {" +
                    "\"title\": \"T-Shirt\"," +
                    "\"body_html\": \"Limp Bisquit\"," +
                    "\"vendor\": \"Burton2\"," +
                    "\"product_type\": \"T-Shirt\"," +
                    "\"variants\": " +
                         "[{ \"option1\": \"First\", \"price\": \"30.00\", \"sku\": \"123\" }]" +
                "}" +
            "}";


            string url = "https://yourstore.myshopify.com/admin/products.json";;
            string verb = "POST";
            string data = newProduct;

            ExecuteRequest(url, verb, data, "[apikey]", "[apiPassword]");




            var query = shopify.products();
            foreach (var product in query.products)
            {
                //System.Diagnostics.Debug.WriteLine(product.title);
                Console.WriteLine(product.title);
            }
			

		// <summary>
        /// The core executor for sending off requests
        /// </summary>
        string ExecuteRequest(string url, string verb, string data, string apikey, string password)
        {

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.PreAuthenticate = true;
            var creds = new NetworkCredential(userName: apikey, password: password);
            request.Credentials = creds;

            request.ContentType = "application/json";
            request.Method = verb;
            //request.Method = WebRequestMethods.Http.Post;
            request.Accept = "*/*";
            //request.ContentLength = 200; 

            //add the data if needed
            if (!String.IsNullOrEmpty(data))
            {
                using (var ms = new MemoryStream())
                {
                    using (var writer = new StreamWriter(request.GetRequestStream()))
                    {
                        writer.Write(data);
                        writer.Close();
                    }
                }
            }





            //var response = (HttpWebResponse)request.GetResponse();
            var response = request.GetResponse() as HttpWebResponse;

            string result = "";

            using (Stream stream = response.GetResponseStream())
            {
                StreamReader sr = new StreamReader(stream);
                result = sr.ReadToEnd();
                sr.Close();
            }
            return result;
        }