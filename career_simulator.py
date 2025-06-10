import streamlit as st

# 職種・スキル・アイコン例（全職種フル）
career_paths = {
    "フロントエンドエンジニア": (["JavaScript", "React", "UI/UX", "HTML/CSS"], "🌐"),
    "バックエンドエンジニア": (["Python", "DB設計", "API開発", "Linux"], "🖥️"),
    "インフラエンジニア": (["Linux", "ネットワーク", "AWS", "監視"], "🛠️"),
    "セキュリティエンジニア": (["セキュリティ基礎", "脆弱性診断", "ネットワーク", "ログ解析"], "🔒"),
    "QAエンジニア": (["テスト設計", "自動化", "品質管理"], "🧪"),
    "データサイエンティスト": (["Python", "Pandas", "機械学習", "SQL"], "📊"),
    "AIエンジニア": (["Python", "AI基礎", "深層学習", "PyTorch"], "🤖"),
    "SRE": (["AWS", "監視", "CI/CD", "障害対応"], "⚙️"),
    "クラウドエンジニア": (["AWS", "Azure", "GCP", "IaC"], "☁️"),
    "テックリード": (["設計力", "レビュー", "リーダーシップ"], "👑"),
    "ITコンサルタント": (["提案力", "要件定義", "IT知識"], "💡"),
    "プロダクトマネージャー": (["企画", "要件定義", "進行管理"], "📋"),
    "ヘルプデスク": (["PCサポート", "トラブル対応", "コミュ力"], "📞"),
    "インフラ支援": (["PC設定", "ネットワーク", "現場対応"], "🔧"),
    "組み込みエンジニア": (["C言語", "マイコン", "ハード制御"], "🔌"),
    "IT営業": (["提案力", "コミュ力", "IT知識"], "🗣️"),
    "人事": (["採用", "研修", "人材育成"], "🧑‍💼"),
    "総務": (["事務", "社内調整", "規程管理"], "📁"),
    "フィールドエンジニア": (["現場対応", "機器設置", "トラブル対応"], "🚗"),
    "社内SE": (["ヘルプデスク", "業務改善", "PC管理"], "🏢"),
    "Webディレクター": (["進行管理", "要件定義", "UI/UX"], "📝"),
    "UI/UXデザイナー": (["Figma", "デザイン思考", "プロトタイピング"], "🎨"),
    "サポートエンジニア": (["顧客対応", "技術サポート", "トラブル対応"], "🛟"),
    "RPAエンジニア": (["RPAツール", "業務分析", "自動化"], "🤖"),
    "IT講師": (["教育", "資料作成", "プレゼン"], "🎤"),
}

# スキル詳細データ（リソース付きで抜粋例。必要に応じて追加してください）
skill_details = {
    "JavaScript": {
        "desc": "Webフロントエンド開発の中心言語。動的なWebページを作る。",
        "order": 1, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "MDN JavaScript", "url": "https://developer.mozilla.org/ja/docs/Web/JavaScript"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=javascript+入門"}
        ]
    },
    "React": {
        "desc": "モダンなWebフロントエンド開発フレームワーク。SPA開発で主流。",
        "order": 2, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "React公式", "url": "https://ja.react.dev/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=react+入門"}
        ]
    },
    "UI/UX": {
        "desc": "ユーザー体験・デザインの基礎。使いやすさを考える力。",
        "order": 3, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "Goodpatch Blog", "url": "https://goodpatch.com/blog/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=ui+ux+入門"}
        ]
    },
    "HTML/CSS": {
        "desc": "Webページの構造とデザインの基礎技術。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "MDN HTML", "url": "https://developer.mozilla.org/ja/docs/Web/HTML"},
            {"label": "MDN CSS", "url": "https://developer.mozilla.org/ja/docs/Web/CSS"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=html+css+入門"}
        ]
    },
    "Python": {
        "desc": "汎用性が高く、Web・AI・データ分析など幅広く使われる言語。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "Python公式", "url": "https://docs.python.org/ja/3/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=python+入門"}
        ]
    },
    "DB設計": {
        "desc": "データベースの設計・運用スキル。効率的なデータ管理の基礎。",
        "order": 1, "period": "1年目", "level": "中級",
        "resource": [
            {"label": "PostgreSQL公式", "url": "https://www.postgresql.jp/document/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=DB設計+入門"}
        ]
    },
    "API開発": {
        "desc": "WebサービスのAPI設計・実装。システム連携の要。",
        "order": 2, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "FastAPI公式", "url": "https://fastapi.tiangolo.com/ja/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=api+開発+入門"}
        ]
    },
    "Linux": {
        "desc": "サーバー運用や開発の基礎OS。インフラ系の必須スキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "Linux入門記事", "url": "https://eng-entrance.com/linux"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=linux+入門"}
        ]
    },
    "ネットワーク": {
        "desc": "ネットワークの基礎知識。インフラやセキュリティ分野で必須。",
        "order": 1, "period": "1年目", "level": "中級",
        "resource": [
            {"label": "ネットワーク入門記事", "url": "https://wa3.i-3-i.info/word124.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=ネットワーク+入門"}
        ]
    },
    "AWS": {
        "desc": "クラウドサービスの代表格。インフラ・クラウド系で必須。",
        "order": 2, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "AWS公式", "url": "https://aws.amazon.com/jp/getting-started/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=aws+入門"}
        ]
    },
    "監視": {
        "desc": "システムやサービスの稼働状況を監視し、障害を早期発見するスキル。",
        "order": 3, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "監視入門記事", "url": "https://www.infraexpert.com/study/monitor.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=サーバー監視+入門"}
        ]
    },
    "セキュリティ基礎": {
        "desc": "情報セキュリティの基本。安全なシステム運用のための知識。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "IPAセキュリティセンター", "url": "https://www.ipa.go.jp/security/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=セキュリティ+基礎+入門"}
        ]
    },
    "脆弱性診断": {
        "desc": "システムの弱点を見つけるスキル。セキュリティ対策の要。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "IPA脆弱性対策", "url": "https://www.ipa.go.jp/security/vuln/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=脆弱性診断+入門"}
        ]
    },
    "ログ解析": {
        "desc": "システムログを分析し、障害や攻撃の兆候を発見するスキル。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "ログ解析入門記事", "url": "https://wa3.i-3-i.info/word126.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=ログ解析+入門"}
        ]
    },
    "テスト設計": {
        "desc": "ソフトウェアの品質を高めるためのテスト計画・設計スキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "テスト設計入門記事", "url": "https://wa3.i-3-i.info/word12641.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=テスト設計+入門"}
        ]
    },
    "自動化": {
        "desc": "テストや運用の自動化。効率化・品質向上に必須。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "Selenium公式", "url": "https://www.selenium.dev/documentation/ja/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=テスト自動化+入門"}
        ]
    },
    "品質管理": {
        "desc": "ソフトウェアやサービスの品質を維持・向上させるスキル。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "品質管理入門記事", "url": "https://wa3.i-3-i.info/word12642.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=品質管理+入門"}
        ]
    },
    "Pandas": {
        "desc": "データ分析のためのPythonライブラリ。",
        "order": 1, "period": "1年目", "level": "中級",
        "resource": [
            {"label": "Pandas公式", "url": "https://pandas.pydata.org/docs/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=pandas+入門"}
        ]
    },
    "機械学習": {
        "desc": "AI・データ分析の基礎。scikit-learnなどで学ぶ。",
        "order": 2, "period": "2年目", "level": "上級",
        "resource": [
            {"label": "scikit-learn公式", "url": "https://scikit-learn.org/stable/user_guide.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=機械学習+入門"}
        ]
    },
    "SQL": {
        "desc": "データベース操作のための言語。データ抽出・集計の基礎。",
        "order": 3, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "SQL入門記事", "url": "https://www.dbonline.jp/sqlite/index.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=sql+入門"}
        ]
    },
    "AI基礎": {
        "desc": "AIの基本概念や仕組みを理解する。",
        "order": 0, "period": "1年目", "level": "中級",
        "resource": [
            {"label": "AI入門記事", "url": "https://www.ossnews.jp/oss_info/AI"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=ai+入門"}
        ]
    },
    "深層学習": {
        "desc": "AIの中でも特に注目される分野。ニューラルネットワークの基礎。",
        "order": 3, "period": "2年目", "level": "上級",
        "resource": [
            {"label": "Deep Learning入門", "url": "https://www.deeplearningbook.org/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=深層学習+入門"}
        ]
    },
    "PyTorch": {
        "desc": "深層学習のためのPythonライブラリ。",
        "order": 4, "period": "3年目", "level": "上級",
        "resource": [
            {"label": "PyTorch公式", "url": "https://pytorch.org/tutorials/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=pytorch+入門"}
        ]
    },
    "CI/CD": {
        "desc": "継続的インテグレーション・継続的デリバリーの自動化技術。",
        "order": 2, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "CI/CD入門記事", "url": "https://www.redhat.com/ja/topics/devops/what-is-ci-cd"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=CI+CD+入門"}
        ]
    },
    "障害対応": {
        "desc": "システム障害発生時の原因特定・復旧・再発防止のスキル。",
        "order": 3, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "障害対応入門記事", "url": "https://wa3.i-3-i.info/word12643.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=障害対応+入門"}
        ]
    },
    "Azure": {
        "desc": "Microsoftのクラウドサービス。クラウドエンジニアに必須。",
        "order": 1, "period": "1年目", "level": "中級",
        "resource": [
            {"label": "Azure公式", "url": "https://learn.microsoft.com/ja-jp/azure/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=Azure+入門"}
        ]
    },
    "GCP": {
        "desc": "Googleのクラウドサービス。クラウドエンジニアに必須。",
        "order": 2, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "GCP公式", "url": "https://cloud.google.com/docs?hl=ja"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=GCP+入門"}
        ]
    },
    "IaC": {
        "desc": "Infrastructure as Code。インフラ構成をコードで管理する技術。",
        "order": 3, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "IaC入門記事", "url": "https://www.redhat.com/ja/topics/automation/what-is-infrastructure-as-code-iac"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=IaC+入門"}
        ]
    },
    "設計力": {
        "desc": "システムやサービスの全体設計・アーキテクチャ設計のスキル。",
        "order": 0, "period": "1年目", "level": "上級",
        "resource": [
            {"label": "設計入門記事", "url": "https://wa3.i-3-i.info/word12644.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=システム設計+入門"}
        ]
    },
    "レビュー": {
        "desc": "コードや設計の品質を高めるためのレビュー技術。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "レビュー入門記事", "url": "https://wa3.i-3-i.info/word12645.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=コードレビュー+入門"}
        ]
    },
    "リーダーシップ": {
        "desc": "チームをまとめ、成果を最大化するためのリーダーシップ。",
        "order": 2, "period": "3年目", "level": "上級",
        "resource": [
            {"label": "リーダーシップ入門記事", "url": "https://www.bizreach.jp/column/leadership/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=リーダーシップ+入門"}
        ]
    },
    "提案力": {
        "desc": "顧客や社内に最適なITソリューションを提案する力。",
        "order": 0, "period": "1年目", "level": "中級",
        "resource": [
            {"label": "提案力入門記事", "url": "https://www.bizreach.jp/column/proposal/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=提案力+入門"}
        ]
    },
    "要件定義": {
        "desc": "システムやサービスの要件を明確にするスキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "要件定義入門記事", "url": "https://wa3.i-3-i.info/word12646.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=要件定義+入門"}
        ]
    },
    "IT知識": {
        "desc": "IT全般の基礎知識。幅広い分野で活躍するための土台。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "ITパスポート公式", "url": "https://www3.jitec.ipa.go.jp/JitesCbt/html/openinfo.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=ITパスポート+入門"}
        ]
    },
    "企画": {
        "desc": "新しいサービスやプロダクトを企画・立案するスキル。",
        "order": 0, "period": "1年目", "level": "中級",
        "resource": [
            {"label": "企画入門記事", "url": "https://www.bizreach.jp/column/planning/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=企画+入門"}
        ]
    },
    "進行管理": {
        "desc": "プロジェクトの進捗や課題を管理し、納期を守るスキル。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "進行管理入門記事", "url": "https://wa3.i-3-i.info/word12647.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=進行管理+入門"}
        ]
    },
    "PCサポート": {
        "desc": "PCや周辺機器のトラブル対応・サポートスキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "PCサポート入門記事", "url": "https://www.pc-master.jp/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=PCサポート+入門"}
        ]
    },
    "トラブル対応": {
        "desc": "システムや機器のトラブルを迅速に解決するスキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "トラブル対応入門記事", "url": "https://wa3.i-3-i.info/word12648.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=トラブル対応+入門"}
        ]
    },
    "コミュ力": {
        "desc": "社内外の関係者と円滑にやりとりするためのコミュニケーション力。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "コミュ力入門記事", "url": "https://www.bizreach.jp/column/communication/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=コミュニケーション+入門"}
        ]
    },
    "PC設定": {
        "desc": "PCやネットワーク機器の初期設定・運用スキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "PC設定入門記事", "url": "https://www.pc-master.jp/first/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=PC設定+入門"}
        ]
    },
    "現場対応": {
        "desc": "現場での機器設置やトラブル対応など、フィールド業務のスキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "現場対応入門記事", "url": "https://www.fieldengineer.com/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=フィールドエンジニア+入門"}
        ]
    },
    "機器設置": {
        "desc": "ネットワークやIT機器の設置・設定スキル。",
        "order": 2, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "機器設置入門記事", "url": "https://www.fieldengineer.com/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=機器設置+入門"}
        ]
    },
    "C言語": {
        "desc": "組み込み開発やハード制御で使われるプログラミング言語。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "C言語入門記事", "url": "https://www.c-lang.net/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=C言語+入門"}
        ]
    },
    "マイコン": {
        "desc": "マイクロコントローラの基礎知識とプログラミング。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "マイコン入門記事", "url": "https://deviceplus.jp/hobby/entry_001/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=マイコン+入門"}
        ]
    },
    "ハード制御": {
        "desc": "ハードウェアをプログラムで制御する技術。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "ハード制御入門記事", "url": "https://monoist.itmedia.co.jp/mn/articles/2002/19/news010.html"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=ハード制御+入門"}
        ]
    },
    "採用": {
        "desc": "人材採用の計画・面接・選考スキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "採用入門記事", "url": "https://jinjibu.jp/keyword/detl/104/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=採用+入門"}
        ]
    },
    "研修": {
        "desc": "新入社員や既存社員への教育・研修スキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "研修入門記事", "url": "https://jinjibu.jp/keyword/detl/105/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=研修+入門"}
        ]
    },
    "人材育成": {
        "desc": "社員の成長を促すための育成・評価スキル。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "人材育成入門記事", "url": "https://jinjibu.jp/keyword/detl/106/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=人材育成+入門"}
        ]
    },
    "事務": {
        "desc": "書類作成やデータ管理などの事務作業スキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "事務入門記事", "url": "https://www.officework.jp/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=事務+入門"}
        ]
    },
    "社内調整": {
        "desc": "社内の各部署と連携し、業務を円滑に進めるスキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "社内調整入門記事", "url": "https://jinjibu.jp/keyword/detl/107/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=社内調整+入門"}
        ]
    },
    "規程管理": {
        "desc": "社内規程やルールの作成・運用・管理スキル。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "規程管理入門記事", "url": "https://jinjibu.jp/keyword/detl/108/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=規程管理+入門"}
        ]
    },
    "ヘルプデスク": {
        "desc": "社内外のITサポート・トラブル対応を行うスキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "ヘルプデスク入門記事", "url": "https://www.helpdesk-japan.com/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=ヘルプデスク+入門"}
        ]
    },
    "業務改善": {
        "desc": "業務フローを見直し、効率化・最適化するスキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "業務改善入門記事", "url": "https://www.bizreach.jp/column/business-improvement/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=業務改善+入門"}
        ]
    },
    "PC管理": {
        "desc": "社内PCやIT資産の管理・運用スキル。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "PC管理入門記事", "url": "https://www.pc-master.jp/first/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=PC管理+入門"}
        ]
    },
    "Figma": {
        "desc": "WebデザインやUI設計で使われるデザインツール。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "Figma公式", "url": "https://www.figma.com/ja/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=figma+入門"}
        ]
    },
    "デザイン思考": {
        "desc": "ユーザー中心の課題解決手法。新規サービス開発で重要。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "デザイン思考入門記事", "url": "https://designthinking.or.jp/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=デザイン思考+入門"}
        ]
    },
    "プロトタイピング": {
        "desc": "アイデアを素早く形にして検証するスキル。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "プロトタイピング入門記事", "url": "https://www.goodpatch.com/blog/prototyping/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=プロトタイピング+入門"}
        ]
    },
    "顧客対応": {
        "desc": "顧客の要望や課題をヒアリングし、最適なサポートを行うスキル。",
        "order": 0, "period": "1年目", "level": "中級",
        "resource": [
            {"label": "顧客対応入門記事", "url": "https://www.bizreach.jp/column/customer-support/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=顧客対応+入門"}
        ]
    },
    "技術サポート": {
        "desc": "技術的な問い合わせやトラブルに対応するスキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "技術サポート入門記事", "url": "https://www.bizreach.jp/column/tech-support/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=技術サポート+入門"}
        ]
    },
    "RPAツール": {
        "desc": "業務自動化のためのRPAツール（UiPathなど）の活用スキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "UiPath公式", "url": "https://www.uipath.com/ja/resources"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=RPA+入門"}
        ]
    },
    "業務分析": {
        "desc": "業務フローを分析し、改善点や自動化ポイントを見つけるスキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "業務分析入門記事", "url": "https://www.bizreach.jp/column/business-analysis/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=業務分析+入門"}
        ]
    },
    "教育": {
        "desc": "ITや業務知識を他者にわかりやすく教えるスキル。",
        "order": 0, "period": "1年目", "level": "初級",
        "resource": [
            {"label": "教育入門記事", "url": "https://www.manabi.st/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=IT教育+入門"}
        ]
    },
    "資料作成": {
        "desc": "分かりやすい資料やスライドを作成するスキル。",
        "order": 1, "period": "2年目", "level": "中級",
        "resource": [
            {"label": "資料作成入門記事", "url": "https://www.slideshare.net/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=資料作成+入門"}
        ]
    },
    "プレゼン": {
        "desc": "自分の考えや成果を分かりやすく伝えるプレゼンテーションスキル。",
        "order": 2, "period": "3年目", "level": "中級",
        "resource": [
            {"label": "プレゼン入門記事", "url": "https://www.bizreach.jp/column/presentation/"},
            {"label": "YouTube入門動画", "url": "https://www.youtube.com/results?search_query=プレゼン+入門"}
        ]
    },
}    # 必要に応じて他スキルも同様に追加してください

all_skills = sorted(set(sum([v[0] for v in career_paths.values()], [])))

st.set_page_config(page_title="キャリアパス・シミュレーター", layout="centered")
st.title("🚀 キャリアパス・シミュレーター")
st.markdown(
    "<span style='color:#1e4fa3;font-weight:bold;'>職種やスキルを選ぶと、キャリアロードマップと学習リソースが表示されます。</span>",
    unsafe_allow_html=True
)
st.image("https://undraw.co/api/illustrations/undraw_career_progress_ivdb.svg", width=220)

current_role = st.selectbox("現在の職種", list(career_paths.keys()))
target_role = st.selectbox("目標職種", list(career_paths.keys()))
current_skills = st.multiselect("今持っているスキル", all_skills)
line_token = st.text_input("LINE Notifyトークン（任意）", type="password")

if st.button("シミュレート", use_container_width=True):
    required_skills = [s for s in career_paths[target_role][0] if s not in current_skills]
    ordered_skills = sorted(required_skills, key=lambda s: skill_details.get(s, {}).get("order", 99))

    st.subheader("🗺️ キャリアロードマップ")
    st.markdown(
        "下のタイムラインは、あなたの現在の職種から目標職種に進むためのステップを淡い色合いで表現しています。"
        "各ステップのアイコンや色を参考に、順番にスキルを身につけていきましょう！"
    )

    pastel_colors = ["#e3f0ff", "#fffbe6", "#ffe6e6", "#e6f7e6", "#f6e6ff", "#e6f7fa", "#fff0e6"]
    timeline = []
    timeline.append({
        "title": f"今：{current_role}",
        "icon": career_paths[current_role][1],
        "color": "#8bb7f0",
        "desc": "現在のあなたの職種",
        "font_color": "#fff"
    })
    for i, skill in enumerate(ordered_skills, 1):
        skill_icon = "⭐"
        if "Python" in skill: skill_icon = "🐍"
        elif "AWS" in skill: skill_icon = "☁️"
        elif "React" in skill: skill_icon = "⚛️"
        elif "UI/UX" in skill or "デザイン" in skill: skill_icon = "🎨"
        elif "DB" in skill or "SQL" in skill: skill_icon = "🗄️"
        elif "Linux" in skill: skill_icon = "🐧"
        elif "AI" in skill or "機械学習" in skill: skill_icon = "🤖"
        elif "ネットワーク" in skill: skill_icon = "🌐"
        elif "テスト" in skill: skill_icon = "🧪"
        elif "自動化" in skill: skill_icon = "⚙️"
        elif "現場" in skill: skill_icon = "🚗"
        elif "教育" in skill or "研修" in skill: skill_icon = "🎤"
        detail = skill_details.get(skill, {})
        timeline.append({
            "title": f"{detail.get('period','')}: {skill_icon} {skill}",
            "icon": skill_icon,
            "color": pastel_colors[i % len(pastel_colors)],
            "desc": f"{detail.get('desc','')}",
            "font_color": "#222",
            "period": detail.get("period", ""),
            "level": detail.get("level", ""),
            "resource": detail.get("resource", [])
        })
    timeline.append({
        "title": f"ゴール：{career_paths[target_role][1]} {target_role}",
        "icon": career_paths[target_role][1],
        "color": "#b2e6c7",
        "desc": "目標職種に到達！",
        "font_color": "#222"
    })

    cols = st.columns(len(timeline))
    for i, step in enumerate(timeline):
        font_color = step.get("font_color", "#222")
        level = step.get("level", "")
        resources = step.get("resource", [])
        st.markdown(
            f"""
            <div style='background:{step["color"]};border-radius:24px;padding:24px 12px 18px 12px;margin-bottom:8px;box-shadow:0 2px 8px #bbb;text-align:center;min-width:120px;'>
                <div style='font-size:2em'>{step["icon"]}</div>
                <div style='font-weight:bold;font-size:1.1em;margin:6px 0 2px 0;color:{font_color};'>{step["title"]}</div>
                <div style='font-size:0.95em;color:{font_color};'>{step["desc"]}</div>
                {"<div style='font-size:0.9em;color:#888;'>レベル: "+level+"</div>" if level else ""}
                {"".join([f"<a href='{res['url']}' target='_blank' style='margin:4px;'><button style='background:#e3f0ff;border:none;border-radius:8px;padding:6px 16px;margin-top:6px;cursor:pointer;'>{res['label']}</button></a>" for res in resources])}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info("例：社内プロジェクト参加、資格取得、勉強会参加、メンター相談などもおすすめ！")
    st.image("https://3.bp.blogspot.com/-6QwQwQwQwQw/WFQwQwQwQwI/AAAAAAABFQw/it_career.png", width=120, caption="キャリアのイメージ（いらすとや）")

st.caption("イラストやアイコンはunDraw・いらすとや・絵文字などを活用しています。")