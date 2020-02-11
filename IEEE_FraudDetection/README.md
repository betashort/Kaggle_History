# Kaggle_IEEE_FraudDetection
IEEE詐欺検出  

## 目的
競争では、バイナリターゲットisFraudで示されるように、オンライン取引が不正である可能性を予測しています。  

データは、IDとトランザクションの2つのファイルに分割され、それらはTransactionIDによって結合されます。
すべてのトランザクションに対応する識別情報があるわけではありません。

## 評価指標
AUC  
area under the ROC curve  

# データについて
Transaction TableとIdentity Table

## Transaction Table
* TransactionDT: timedelta from a given reference datetime (not an actual timestamp)

* TransactionAMT: transaction payment amount in USD
取引額
* ProductCD: product code, the product for each transaction
製品コード
* card1 - card6: payment card information, such as card type, card category, issue bank, country, etc.
カード情報
* addr: address
アドレス
* dist: distance

* P_ and (R__) emaildomain: purchaser and recipient email domain
メールドメイン
* C1-C14: counting, such as how many addresses are found to be associated with the payment card, etc. The actual meaning is masked.

* D1-D15: timedelta, such as days between previous transaction, etc.
取引間の時間差分
* M1-M9: match, such as names on card and address, etc.
カードやアドレスの名前
* Vxxx: Vesta engineered rich features, including ranking, counting, and other entity relations.
Vestaが作った特徴量

Categorical Features:
ProductCD
card1 - card6
addr1, addr2
Pemaildomain Remaildomain
M1 - M9
## Identity table
network connection information (IP, ISP, Proxy, etc)  
digital signature (UA/browser/os/version, etc) associated with transactions.  
They're collected by Vesta’s fraud protection system and digital security partners.  

Categorical Features:
DeviceType
DeviceInfo
id12 - id38

# Kernel_reviews

## 🕵️ IEEE Fraud Detection - First Look and EDA

競争では、バイナリターゲットisFraudで示されるように、オンライン取引が不正である可能性を予測しています。  

データは、IDとトランザクションの2つのファイルに分割され、それらはTransactionIDによって結合されます。
すべてのトランザクションに対応する識別情報があるわけではありません。

`TransactionDT`機能は与えられた参照日時からのタイムデルタです（実際のタイムスタンプではありません）。
データに関する1つの初期の発見は、列車とテストが時間によって分割されるように見えるということです。
それらの間にはわずかなギャップがありますが、
それ以外の場合、トレーニングセットは以前の期間からのものであり、テストは後の期間からのものです。
 これはどのクロスバリデーションテクニックを使うべきかに影響します。

trainとtestの間の特徴量の分布の違いを検討するときに、これについてさらに検討します。
