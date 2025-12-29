CSSの詳細度
※背景色が灰色が適用されるパターン
```HTML
<!DOCTYPE html>
<html lang="ja">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>CSSの詳細度</title>
		<style>
			.box {
				background-color: red;
			}

			.box {
				width: 100px;
				height: 100px;
				background-color: #ccc;
			}
		</style>
	</head>
	<body>
		<div class="box"></div>
	</body>
</html>
```
※背景色が赤色が適用されるパターン
```HTML
<!DOCTYPE html>
<html lang="ja">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>CSSの詳細度</title>
		<style>
			div.box {
				background-color: red;
			}

			.box {
				width: 100px;
				height: 100px;
				background-color: #ccc;
			}
		</style>
	</head>
	<body>
		<div class="box"></div>
	</body>
</html>
```
### 詳細度
- スタイルの優先順位を決める仕組み
- セレクタの種類や数によって決まる
- 柔軟なCSS設計が可能

### 詳細度の4要素
優先順位順
1. A：インラインスタイル
> [!example]- 例
> ```html
> <div style="background-color: #000"></div>
> ```
2. B：IDセレクター
> [!example]- 例：IDセレクター
><!-- detail:start -->
> ```html
> <style>
> 	#box1 {
> 		background-color: #0f0;
> 	}
> <styel>
>
> <div id="box" class="box"></div>
> ```
> <!-- detail:end -->
1. C：クラス、属性、擬似クラス
> [!example]- 例：クラス
><!-- detail:start -->
> ```html
> <style>
> 	.box {
> 		background-color: #00f;
> 	}
> <styel>
>
> <div id="box" class="box"></div>
> ```
> <!-- detail:end -->

> [!example]- 例：属性
><!-- detail:start -->
> ```html
> <style>
> 	[class="box"] {
> 		background-color: #0ff;
> 	}
> <styel>
>
> <div id="box" class="box"></div>
> ```
> <!-- detail:end -->

> [!example]- 例：擬似クラス
><!-- detail:start -->
> ```html
> <style>
> 	.box:hover {
> 		background-color: #ff0;
> 	}
> <styel>
>
> <div id="box" class="box"></div>
> ```
> <!-- detail:end -->
2. D：タイプ、擬似要素
 > [!example]- 例：タイプ
><!-- detail:start -->
> ```html
> <style>
> 	div {
> 		background-color: #0f0;
> 	}
> <styel>
>
> <div id="box"></div>
> ```
> <!-- detail:end -->

> [!example]- 例：擬似要素
><!-- detail:start -->
> ```html
> <style>
> 	div::befor {
> 		content: "★";
> 	}
> <styel>
>
> <div id="box"></div>
> ```
> <!-- detail:end -->
### 詳細度の加算
- 同一優先度の加算ありと加算なしの場合
	- →加算されている方が優先される

- 加算あり同士だが、優先度に差がある場合
	- →優先度が高い方が優先される
		　例：CとDの加算とDとDの加算→CとDの加算が優先
### !importantによる強制優先度設定
- 最強ルール
	- 詳細度を強制的に上書き
- 使用注意
	- 強制力が強いため、詳細度が複雑になるため避けるべき
- 緊急時のみ
	- 最終手段として限定使用
		例： CMSのツールから吐き出しているCSSを修正したい場合など特殊事例など
