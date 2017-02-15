# ベイジアンフィルタとは
ナイーブベイズというアルゴリズムを用いて、テキストの自動分類に応用の出来るフィルタの総称
メールのスパム判定や、ブログのカテゴリ分類など

# ナイーブベイズのアルゴリズム
ナイーブベイズは確率論に基づいたアルゴリズム
これを使ってのカテゴリの推定とは、ある文章が与えられたとき、どのカテゴリに属するのかもっともらしいのか
単語の出現確率から求める。
このもっともらしいというものを統計学では尤度と呼ぶ