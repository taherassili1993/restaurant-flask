db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'restaurant-flask'
    }
sql = "CREATE TABLE if not exists `users` ( `id` int(11) NOT NULL AUTO_INCREMENT, `email` varchar(255) COLLATE utf8_bin NOT NULL, `name` varchar(255) COLLATE utf8_bin NOT NULL, `password` varchar(255) COLLATE utf8_bin NOT NULL, PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1 ;"

sql_restaurant = "CREATE TABLE if not exists `restaurants` ( `id` int(11) NOT NULL AUTO_INCREMENT, `nom` varchar(255) COLLATE utf8_bin NOT NULL, `telephone` varchar(255) COLLATE utf8_bin NOT NULL, `addresse` varchar(255) COLLATE utf8_bin NOT NULL, `user_id` varchar(255) COLLATE utf8_bin NOT NULL, PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1 ;"
