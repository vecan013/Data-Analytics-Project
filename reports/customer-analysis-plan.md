Objective:-
Prepare an analysis plan for understanding customer purchasing behavior.

Assigned to: C.R.Adharsh

1. Identify the customer and order tables.

olist_customers_dataset.csv --> Customer identifiers and location

olist_orders_dataset.csv --> Order-to-customer mapping, purchase dates, and statuses

olist_order_items_dataset.csv --> Items and item-level costs in each order

2. Explain the difference between customer_id and customer_unique_id.

customer_id: identifies the customer record linked to an order.

customer_unique_id: identifies the underlying customer across potentially multiple customer records.

3. Define how repeat customers will be identified.

* One-time customer: one eligible order.
* Repeat customer: two or more distinct eligible orders.

Repeat-customer rate = repeat customers / all eligible unique customers × 100

4. Propose customer location and purchasing-pattern analyses.

Customer location analysis will be performed using the customer_city, customer_state, and customer_zip_code_prefix columns from the customer dataset.

Customer Distribution by State:

customer_state,unique_customers,orders,item_revenue,freight_total
SP,39156,40501,5067633.16,702069.99
RJ,11917,12350,1759651.1300000001,295750.44
MG,11001,11354,1552481.83,266409.84
RS,5168,5345,728897.47,132575.32
PR,4769,4923,666063.51,115645.29
SC,3449,3546,507012.13,88115.65
BA,3158,3256,493584.14,97553.67
DF,2019,2080,296498.41,49624.94
ES,1928,1995,268643.45,49014.48
GO,1895,1957,282836.7,51375.65
PE,1551,1593,251889.49,57082.56
CE,1258,1279,219757.38,46679.39
PA,922,946,174470.59,37552.98
MT,856,886,152191.62,29032.8
MA,700,717,117009.38,30794.17
MS,681,701,115429.97,18937.579999999998
PB,504,517,112586.82,25251.73
PI,464,476,84721.0,20457.19
RN,464,474,82105.66,18609.12
AL,387,397,78855.72,15316.77
SE,329,335,56574.19,13714.94
TO,267,274,48402.51,11604.86
RO,231,243,45682.76,11283.24
AM,140,145,22155.84,5429.63
AC,76,80,15930.97,3644.36
AP,66,67,13374.81,2767.0
RR,40,41,7057.47,1982.05


Customer Distribution by City:

customer_state,customer_city,unique_customers,orders,item_revenue
SP,sao paulo,14528,15045,1859556.83
RJ,rio de janeiro,6361,6601,955573.97
MG,belo horizonte,2606,2697,346039.04
DF,brasilia,2013,2071,295814.72
PR,curitiba,1434,1489,205999.33
SP,campinas,1363,1406,184657.87
RS,porto alegre,1292,1342,182319.55
BA,salvador,1154,1188,173273.05
SP,guarulhos,1111,1144,139008.19
SP,sao bernardo do campo,881,911,102514.23
RJ,niteroi,788,825,115890.26
SP,santo andre,750,777,89380.83
SP,osasco,697,724,80820.34
SP,santos,680,700,98349.4
SP,sao jose dos campos,644,667,75425.31
GO,goiania,641,660,96547.85
CE,fortaleza,609,618,93269.67
SP,sorocaba,588,609,74638.18
PE,recife,571,593,85186.33
SC,florianopolis,535,556,84043.85
SP,jundiai,532,549,80398.04
SP,ribeirao preto,479,499,64672.27
PA,belem,418,428,78002.75
RJ,nova iguacu,415,423,58217.83
MG,juiz de fora,412,423,64456.78
MG,contagem,406,415,48561.04
SP,barueri,406,419,49995.71
RJ,sao goncalo,377,385,50833.27
SP,mogi das cruzes,362,374,50295.68
ES,vitoria,360,373,52038.6
MG,uberlandia,360,367,47560.57
SP,piracicaba,349,356,49173.47
MA,sao luis,326,335,50141.82
SP,sao jose do rio preto,324,329,46669.73
ES,vila velha,317,326,46895.83
SP,carapicuiba,309,316,31769.85
SP,maua,308,317,43360.96
MS,campo grande,308,312,56513.68
PR,londrina,290,298,45867.97
SP,praia grande,278,296,38303.17
SP,taboao da serra,274,284,34740.69
ES,serra,272,278,35184.07
SP,diadema,265,276,28839.98
SP,indaiatuba,263,274,36862.6
SP,sao caetano do sul,262,272,32159.8
PI,teresina,261,271,49028.57
SP,taubate,257,260,28887.1
SP,bauru,257,263,38903.69
SC,joinville,254,257,34399.99
PR,maringa,251,260,37299.2
RJ,duque de caxias,247,250,32769.23
MT,cuiaba,237,243,38178.84
SP,cotia,236,242,29713.74
PB,joao pessoa,234,245,51502.15
AL,maceio,233,236,43592.59
RJ,campos dos goytacazes,229,232,32413.58
RJ,macae,222,228,30525.43
SP,sao carlos,221,231,29511.11
RJ,volta redonda,221,227,33329.1
SP,suzano,218,230,24549.9
RJ,petropolis,216,234,32247.68
SP,americana,212,216,24462.18
RS,caxias do sul,210,220,36033.19
SE,aracaju,209,213,34485.94
SP,guaruja,207,217,28878.39
MG,montes claros,202,207,25967.15
RN,natal,199,203,35751.38
RS,canoas,197,205,26470.14
MG,betim,195,196,27863.71
SP,marilia,193,194,33664.13
RS,santa maria,187,193,31644.82
SP,jacarei,185,189,18055.78
RS,pelotas,178,183,22257.23
MG,uberaba,177,186,27338.65
SP,limeira,177,186,22804.26
SC,blumenau,176,181,24240.08
SP,valinhos,176,181,22101.75
SP,sumare,173,178,21274.11
BA,feira de santana,173,181,26694.2
SP,santana de parnaiba,172,178,23029.75
SP,itapevi,169,170,18348.91
MG,ipatinga,166,169,21797.420000000002
SP,itaquaquecetuba,164,168,18889.92
SC,sao jose,164,167,20251.46
SP,presidente prudente,155,157,25517.329999999998
SP,sao vicente,155,157,18969.19
SP,embu das artes,154,157,19998.78
SP,franca,153,154,22015.55
SP,atibaia,149,154,20343.73
SP,rio claro,146,151,19555.58
SP,araraquara,145,150,19871.850000000002
PR,cascavel,144,146,23275.82
SP,hortolandia,140,142,16225.15
SP,braganca paulista,140,144,20127.62
RJ,nova friburgo,135,142,27345.1
PR,ponta grossa,133,141,18573.48
MG,governador valadares,133,134,18106.35
SP,aracatuba,133,138,16589.39
ES,cariacica,132,135,16386.68
AM,manaus,132,137,20451.56
MG,divinopolis,131,132,34932.97
PE,jaboatao dos guararapes,130,131,21143.170000000002
RJ,marica,130,133,15216.26
RJ,rio das ostras,128,130,18998.99
SP,itu,126,129,12266.34
PR,sao jose dos pinhais,125,130,14899.05
SP,paulinia,122,127,16475.05
MG,pouso alegre,122,128,21181.45
MG,sete lagoas,121,126,17263.35
RJ,sao joao de meriti,121,124,17777.56
RS,rio grande,118,121,16189.98
RS,novo hamburgo,118,121,17547.13
ES,cachoeiro de itapemirim,117,121,15871.630000000001
RJ,barra mansa,117,119,18698.98
SC,itajai,117,119,18698.57
SP,santa barbara d'oeste,117,118,13072.08
RJ,teresopolis,114,119,17115.29
RJ,resende,113,115,13390.35
RJ,cabo frio,112,113,16016.52
MG,pocos de caldas,111,116,15620.68
RS,passo fundo,111,112,15163.71
GO,anapolis,108,111,17129.88
RS,gravatai,107,111,18591.02
SP,ribeirao pires,106,107,10149.63
SP,ferraz de vasconcelos,105,109,15549.53
SP,franco da rocha,103,108,10073.2
RJ,belford roxo,102,104,12205.36
RJ,nilopolis,101,103,13127.18
RJ,mage,101,106,14316.76
GO,aparecida de goiania,100,105,14203.98
RS,sao leopoldo,100,103,11037.67
RO,porto velho,100,108,21890.55
SP,botucatu,98,100,17104.51
SC,chapeco,97,101,15106.11
MG,patos de minas,96,99,16726.98
SP,cajamar,95,97,9725.38
SP,guaratingueta,95,96,14751.119999999999
SC,balneario camboriu,95,97,16609.329999999998
SP,caieiras,94,97,12662.83
SP,itatiba,94,97,12049.31
MG,nova lima,93,96,20815.15
SP,pindamonhangaba,93,98,12480.28
MG,ribeirao das neves,93,98,12584.54
SP,itapecerica da serra,92,93,8399.01
SC,criciuma,91,91,13725.08
MG,itajuba,89,92,13667.8
SP,francisco morato,89,94,8344.17
SC,palhoca,89,90,10910.460000000001
SP,vinhedo,89,90,8895.12
PE,olinda,88,89,12690.08
MG,santa luzia,88,89,11199.17
SP,salto,88,89,10184.03
SP,araras,88,93,13187.38
TO,palmas,87,88,17420.62
BA,vitoria da conquista,87,88,16234.2
MG,vicosa,85,87,16052.35
SP,mogi-guacu,85,89,11629.82
SC,jaragua do sul,84,88,12924.66
PR,foz do iguacu,84,86,11506.380000000001
MG,varginha,83,88,13933.1
SP,votorantim,83,84,10757.470000000001
SP,caraguatatuba,82,83,11603.26
PA,ananindeua,82,85,17709.44
MG,conselheiro lafaiete,81,82,9061.460000000001
SP,poa,81,85,9343.45
SC,lages,80,83,11281.11
RJ,angra dos reis,80,83,18693.24
SP,assis,79,84,12199.23
SP,jandira,78,84,8260.47
MG,lavras,78,80,12790.960000000001
SP,lorena,77,82,7650.03
MG,itabira,77,77,10069.51
SP,itapetininga,76,77,12232.88
SP,cubatao,76,79,6996.03
SP,ourinhos,76,77,12543.03
SP,birigui,75,78,14611.34
MG,araxa,75,75,13046.42
SP,sao joao da boa vista,74,80,11627.81
SP,mairipora,74,75,9087.38
RJ,mesquita,73,75,9132.02
MG,teofilo otoni,73,75,7744.23
MG,barbacena,73,79,12201.44
SP,sao roque,73,75,9433.18
SP,itanhaem,72,74,9727.09
RJ,araruama,72,74,16889.31
SP,tatui,71,72,11281.03
SP,jau,71,73,9460.56
BA,lauro de freitas,70,72,8632.98
SP,mogi mirim,70,75,8833.97
SP,varzea paulista,70,75,10281.380000000001
SP,cacapava,70,72,9928.07
SP,ubatuba,69,72,8195.93
BA,ilheus,69,69,8546.76
PR,toledo,69,70,10053.64
SP,barretos,68,69,9077.11
RS,viamao,68,70,6479.31
RS,cachoeirinha,68,72,9297.25
SP,catanduva,68,72,9680.83
PB,campina grande,67,67,17410.54
SP,pirassununga,67,69,8550.33
PR,pinhais,66,66,8682.82
AC,rio branco,65,69,13852.34
MG,sao joao del rei,65,66,8168.070000000001
SP,aruja,65,68,7606.78
MG,manhuacu,64,64,8510.0
ES,guarapari,63,66,10494.41
MG,muriae,63,63,10949.43
PE,caruaru,63,63,9265.7
GO,rio verde,63,63,9398.51
SP,avare,62,63,8382.97
PE,petrolina,62,62,13759.1
SP,votuporanga,61,63,8372.9
RS,bage,61,62,8936.64
PR,guarapuava,61,62,8460.550000000001
ES,colatina,61,63,6866.5199999999995
ES,linhares,61,64,11925.11
MG,caratinga,61,62,9690.26
SP,sertaozinho,60,61,6724.2300000000005
RS,santa cruz do sul,60,62,10360.88
SP,jaguariuna,60,60,8312.47
MT,rondonopolis,59,64,10644.04
MG,paracatu,59,62,8376.42
BA,itabuna,58,60,7874.55
SP,amparo,58,63,11395.73
MS,dourados,58,63,8849.71
BA,camacari,58,60,7240.24
PR,colombo,57,60,7386.900000000001
SC,brusque,57,60,8421.55
PR,paranagua,56,58,7339.46
SC,tubarao,55,60,10606.130000000001
SP,sao sebastiao,55,56,7673.46
MG,lagoa santa,55,58,8378.6
RN,parnamirim,55,57,7305.32
MG,ouro preto,54,55,6711.5599999999995
PR,campo mourao,54,56,7259.52
GO,jatai,54,54,10040.37
SP,cruzeiro,54,56,6109.5
MG,unai,53,54,6825.39
MG,araguari,53,54,10869.52
MG,itauna,53,56,7743.95
SP,lins,53,54,9162.66
RJ,itaborai,53,56,6555.85
RJ,queimados,52,53,5841.85
RS,erechim,52,56,6420.89
AP,macapa,52,53,11352.43
PR,araucaria,52,54,5086.1
SP,tupa,52,52,6483.03
SP,fernandopolis,52,52,7415.16
MG,uba,51,53,6369.76
SP,matao,51,51,7162.72
RS,bento goncalves,51,53,6648.58
SP,itapeva,51,52,6360.23
PR,pato branco,51,53,9047.64
RS,alvorada,50,50,6207.7300000000005
SP,itapira,50,52,6933.03
SP,bebedouro,50,51,4992.89
BA,barreiras,50,51,10809.03
RS,ijui,50,52,5584.45
PR,apucarana,49,51,6684.360000000001
MG,timoteo,49,52,7697.87
PR,francisco beltrao,49,50,7291.58
MG,nova serrana,49,49,7447.26
SP,jaboticabal,49,50,5747.12
SP,leme,48,50,8152.92
SP,cosmopolis,48,50,6668.9
RS,uruguaiana,47,47,4414.06
RS,lajeado,47,50,8068.41
RJ,barra do pirai,46,49,5059.2
MG,joao monlevade,46,50,6941.9
SP,bertioga,46,47,9385.65
SC,concordia,46,47,5503.59
SP,campo limpo paulista,46,47,4773.44
SP,embu-guacu,45,46,6244.68
SP,boituva,45,47,6852.15
RJ,itaguai,45,46,6122.54
MG,ibirite,45,47,7241.58
RJ,itaperuna,44,46,5563.58
MG,ituiutaba,44,53,5431.17
SC,videira,44,44,7822.35
SP,registro,44,45,5929.57
RJ,sao pedro da aldeia,44,46,4672.43
MG,patrocinio,44,45,6747.54
PR,paranavai,44,45,7120.95
SP,lencois paulista,43,43,6720.22
MG,passos,43,43,4247.28
SP,ilhabela,43,44,3180.38
ES,sao mateus,43,47,6569.97
SC,sao bento do sul,43,44,4869.9
SC,itapema,42,44,6109.87
SP,louveira,42,44,4777.82
BA,juazeiro,42,42,7401.28
SP,sao jose do rio pardo,42,44,5106.24
SP,vargem grande paulista,42,43,4634.55
MG,alfenas,42,43,5350.32
SP,peruibe,42,43,6531.12
SP,itupeva,42,42,5101.71
PA,santarem,42,43,5287.67
RS,santo angelo,42,45,5333.46
MS,tres lagoas,41,42,7431.320000000001
MT,sinop,41,43,6164.65
PE,paulista,41,41,5736.77
MG,coronel fabriciano,40,40,4149.2
MG,vespasiano,40,41,5953.69
MG,pedro leopoldo,40,40,5057.01
SP,mongagua,40,41,5212.53
SP,artur nogueira,40,40,5949.7
MG,tres coracoes,40,41,4493.83
MG,pirapora,40,42,6803.07
MG,curvelo,40,42,5248.01
MG,sabara,40,42,4481.78
SC,cacador,40,40,4569.38
RS,sapucaia do sul,39,39,5397.84
MA,imperatriz,39,40,7171.38
RS,esteio,39,39,6068.71
PR,umuarama,39,40,5770.52
MG,ouro branco,39,41,4419.23
BA,alagoinhas,39,40,6249.2300000000005
RR,boa vista,39,40,6967.57
BA,paulo afonso,39,39,6492.59
SC,sao miguel do oeste,39,39,6095.82
MG,ponte nova,38,39,6847.89
SP,andradina,38,40,6302.53
MG,bom despacho,38,38,4680.53
ES,aracruz,38,40,4064.07
RJ,saquarema,38,45,4534.05
RS,capao da canoa,38,38,4692.09
SP,nova odessa,37,37,4352.71
TO,araguaina,37,38,7384.79
PR,cianorte,37,39,4863.67
GO,caldas novas,36,36,5301.63
BA,luis eduardo magalhaes,36,36,8343.87
BA,guanambi,36,36,4189.81
SP,monte mor,36,38,4517.2
SP,tremembe,36,38,4876.03
MT,varzea grande,36,37,6630.35
BA,porto seguro,36,39,10241.09
PR,campo largo,36,36,3849.9900000000002
RJ,tres rios,36,38,7172.62
SP,penapolis,36,37,4776.58
SP,olimpia,36,36,5643.54
GO,valparaiso de goias,36,37,5437.85
MG,extrema,36,39,4473.03
CE,caucaia,35,35,5856.66
SP,tiete,35,35,4111.22
MG,para de minas,35,37,7162.08
BA,eunapolis,35,36,6788.610000000001
GO,itumbiara,35,35,5092.22
RJ,paracambi,35,35,6571.96
RS,campo bom,35,35,4264.81
BA,jequie,34,34,4687.84
RS,osorio,34,35,6251.24
RJ,japeri,34,34,4458.27
GO,formosa,34,34,5282.15
SP,pedreira,34,36,2893.6
MG,sao sebastiao do paraiso,34,35,4800.05
PR,almirante tamandare,34,35,4255.69
RJ,vassouras,34,36,4481.9
SP,adamantina,34,35,5393.07
SP,guaira,34,36,3698.54
MG,santa rita do sapucai,34,35,3910.7
RN,mossoro,34,35,4635.47
RS,alegrete,34,35,4483.77
CE,sobral,33,33,10648.85
SP,santa cruz do rio pardo,33,34,2442.48
SC,rio do sul,33,35,4777.85
SP,taquaritinga,33,33,4604.03
SP,capivari,32,32,4663.71
MG,formiga,32,32,4407.94
MG,mariana,32,33,4416.58
PR,telemaco borba,32,34,4693.49
BA,valenca,32,35,6373.59
SP,santa fe do sul,32,34,3945.77
RJ,seropedica,32,33,4391.15
SC,imbituba,31,31,2968.47
CE,juazeiro do norte,31,31,6698.0
SP,mococa,31,33,6020.97
SP,sao joaquim da barra,31,34,4302.49
MG,cataguases,31,32,4474.87
RS,montenegro,31,32,4910.6
PR,arapongas,31,32,6325.0599999999995
MG,guaxupe,31,37,6081.17
PE,camaragibe,31,33,2625.08
MG,sao lourenco,30,32,4207.99
GO,luziania,30,33,4761.46
GO,catalao,30,33,5354.04
SP,promissao,30,31,4189.85
RS,cachoeira do sul,30,30,4480.32
MG,congonhas,30,30,2938.61
SP,monte alto,30,32,2355.01
RS,gramado,29,29,3123.34
CE,maracanau,29,31,4813.33
RS,santa rosa,29,32,2922.14
RS,cruz alta,29,30,2842.11
SP,ibiuna,29,31,3439.52
SP,mirassol,29,29,5850.89
SC,navegantes,29,31,6783.17
RS,guaiba,29,31,5417.51
RJ,santo antonio de padua,29,30,5090.91
RJ,miguel pereira,28,28,3602.2
PR,fazenda rio grande,28,29,4655.49
MG,piumhii,28,28,3707.31
SP,cerquilho,28,30,3299.91
SP,itapolis,28,28,3363.99
SC,gaspar,28,29,10623.34
MG,itabirito,28,28,5012.23
SP,ituverava,28,28,3748.7400000000002
AL,arapiraca,28,29,8728.71
SC,xanxere,28,29,4175.87
MG,alem paraiba,28,28,2870.56
PR,marechal candido rondon,28,30,3469.71
SC,canoinhas,27,27,4583.01
BA,teixeira de freitas,27,28,3386.18
PR,cambe,27,27,3930.67
SP,dracena,27,27,4538.05
MG,diamantina,27,27,2424.28
SP,orlandia,27,28,4027.32
MS,corumba,27,27,4700.17
MT,primavera do leste,27,28,6232.81
RJ,valenca,27,27,3940.46
SC,tijucas,27,30,3504.74
RS,farroupilha,27,27,3213.0299999999997
SP,garca,27,27,2918.41
PR,uniao da vitoria,27,29,5081.929999999999
BA,santo antonio de jesus,27,29,4296.86
SP,itarare,26,28,3915.3
SC,camboriu,26,27,3058.19
RJ,armacao dos buzios,26,28,4817.41
SC,indaial,26,26,3334.7400000000002
SP,jales,26,28,2918.15
RS,santiago,26,26,2304.7000000000003
RJ,rio bonito,26,27,4352.11
SC,joacaba,26,26,4721.0
SP,santa isabel,26,28,2785.66
MG,brumadinho,26,26,2258.23
SP,barra bonita,26,28,3902.4300000000003
SP,porto ferreira,25,26,1646.22
MT,caceres,25,25,4750.1900000000005
PR,dois vizinhos,25,27,2311.92
SP,cachoeira paulista,25,25,3292.0
RS,tramandai,25,25,2703.52
SC,mafra,25,25,1719.6299999999999
PA,altamira,25,25,5168.15
MG,caete,25,27,2482.9700000000003
PR,matinhos,25,27,2862.15
SP,batatais,25,27,5559.93
MG,nanuque,24,25,2395.9700000000003
MG,carangola,24,25,4281.27
MT,barra do garcas,24,25,4076.2000000000003
PA,parauapebas,24,27,4092.06
RJ,cordeiro,24,24,2604.86
RJ,arraial do cabo,24,28,5176.55
PE,garanhuns,24,30,3948.48
GO,trindade,24,24,3425.57
GO,mineiros,24,25,3379.3
RS,venancio aires,24,26,2764.62
SP,ilha solteira,24,24,2299.44
MG,arcos,24,25,5391.7300000000005
PR,rolandia,24,24,5133.94
PR,cornelio procopio,24,24,2234.17
MG,frutal,24,24,3310.46
RS,sapiranga,23,23,3375.7
SP,rio grande da serra,23,25,2169.31
MT,lucas do rio verde,23,23,5667.76
SP,cravinhos,23,24,2363.95
SP,holambra,23,23,2719.2
TO,gurupi,23,24,5229.29
SP,aparecida,23,25,3740.96
MT,tangara da serra,23,23,3905.7
RS,carazinho,23,23,2030.93
SP,campos do jordao,23,25,3201.1
GO,aguas lindas de goias,23,24,2219.91
SP,capao bonito,23,28,3078.97
RJ,sao fidelis,23,23,2029.25
SC,biguacu,22,22,3270.23
SP,presidente venceslau,22,22,2940.19
MG,monte carmelo,22,23,2869.14
PR,irati,22,22,2455.22
BA,dias d'avila,22,23,2468.45
SP,piedade,22,22,2523.87
SP,presidente epitacio,22,23,2572.52
MG,coromandel,22,25,2403.93
PA,maraba,22,22,3597.17
SP,aguas de lindoia,22,22,3092.59
RS,sao gabriel,22,23,2362.85
SP,mairinque,22,24,2772.12
SP,ibitinga,22,22,2911.26
MG,salinas,22,22,4986.7699999999995
MG,santa barbara,22,25,4608.21
PR,castro,22,22,2847.19
BA,jacobina,22,23,7029.76
PI,parnaiba,22,22,3910.11
BA,simoes filho,21,21,4671.48
MG,campo belo,21,21,1836.34
MG,oliveira,21,22,2579.0
PA,castanhal,21,21,3628.62
PR,medianeira,21,21,2883.5299999999997
SP,pederneiras,21,21,3007.0699999999997
RJ,guapimirim,21,21,2967.2599999999998
MG,santos dumont,21,22,2056.3
SC,icara,21,21,2317.34
MG,januaria,21,22,3471.23
ES,viana,21,21,3371.8199999999997
PE,cabo de santo agostinho,21,21,2877.95
CE,aracati,21,21,2629.54
MG,pitangui,21,22,2517.23
MG,machado,21,21,2761.92
RS,taquara,21,21,4427.54
SP,porto feliz,21,21,2974.07
SP,rancharia,20,21,2623.29
RJ,cachoeiras de macacu,20,20,1918.26
SC,garopaba,20,22,2669.1
MG,cambui,20,22,3133.7400000000002
RJ,bom jesus do itabapoana,20,20,3405.91
BA,brumado,20,21,2628.85
SP,piracaia,20,21,2466.93
RS,santana do livramento,20,20,4248.23
MT,sorriso,20,20,3342.75
RS,marau,20,22,2167.34
SC,curitibanos,20,20,2878.94
SC,braco do norte,20,20,2962.4700000000003
SP,juquitiba,20,21,3073.87
MG,sao gotardo,20,20,2479.38
RS,vacaria,20,21,2294.08
RJ,casimiro de abreu,19,20,3458.33
MG,tres pontas,19,19,2228.21
SP,sao manuel,19,20,3052.39
SP,santo antonio de posse,19,20,5027.89
RS,carlos barbosa,19,19,2554.79
RS,ibiruba,19,20,3155.8
SP,monte azul paulista,19,19,2887.91
MG,monte siao,19,20,2530.28
MG,capelinha,19,19,2562.96
SP,paraguacu paulista,19,20,2766.8
RS,estancia velha,19,20,2782.1
SP,tambau,18,19,1513.43
SP,socorro,18,19,2319.45
RJ,iguaba grande,18,19,2348.6
MG,guanhaes,18,18,1931.45
MG,sarzedo,18,18,987.9300000000001
SP,espirito santo do pinhal,18,18,2160.02
SP,viradouro,18,18,2081.54
MG,espera feliz,18,19,3315.75
RS,veranopolis,18,18,2394.04
SC,ararangua,18,18,2246.55
SP,pereira barreto,18,18,4044.82
PR,quatro barras,18,18,1763.66
SP,nova granada,18,19,1790.33
SP,conchal,18,19,2075.2400000000002
RJ,paraty,18,19,2780.77
RS,guapore,18,18,3153.15
CE,crato,18,18,3100.66
PR,palmas,18,19,1921.3799999999999
SP,bonfim paulista,18,18,2457.37
MG,bambui,18,18,2206.67
MG,claudio,18,20,2867.07
PR,laranjeiras do sul,18,19,1995.57
MG,barao de cocais,18,18,1958.4
BA,itapetinga,17,18,2727.12
ES,alegre,17,17,2884.07
PR,jaguariaiva,17,17,1634.5900000000001
SP,laranjal paulista,17,17,2209.33
RJ,miracema,17,17,1547.26
RS,canela,17,17,2418.63
SP,jarinu,17,18,1410.48
PR,mandaguari,17,18,5039.15
SC,timbo,17,20,3957.67
RJ,paraiba do sul,17,18,2949.57
RS,santo antonio da patrulha,17,17,5100.08
MG,visconde do rio branco,17,18,1557.3400000000001
SP,iracemapolis,17,18,1251.88
BA,senhor do bonfim,17,18,2387.38
PI,floriano,17,18,2424.02
PI,picos,17,17,3300.43
MG,leopoldina,17,17,1667.77
SP,guararapes,17,18,1220.84
RS,dois irmaos,17,17,3398.76
MT,juina,17,17,4695.32
SP,palmital,17,18,1760.16
RS,panambi,17,17,3640.9900000000002
PR,sarandi,17,17,1734.93
RS,igrejinha,17,17,1173.03
GO,goianesia,17,17,1987.48
BA,cruz das almas,17,18,2007.24
SP,cerqueira cesar,17,18,3701.52
RJ,itatiaia,17,18,1526.46
SP,pompeia,17,17,1907.08
ES,piuma,17,17,2216.18
ES,castelo,17,18,1600.8
ES,nova venecia,17,19,2439.9
SP,agudos,16,16,1265.3
MA,caxias,16,16,1790.55
MG,ouro fino,16,16,2511.84
SP,santa rita do passa quatro,16,18,2123.9700000000003
MG,caxambu,16,16,1700.73
GO,uruacu,16,17,1750.02
MG,carmo do paranaiba,16,16,4008.64
ES,marataizes,16,16,2907.27
MA,balsas,16,17,5274.43
RS,torres,16,17,1416.23
RO,ji-parana,16,17,3412.04
MG,manhumirim,16,16,2461.7799999999997
SP,cajati,16,16,1821.3200000000002
SP,pitangueiras,16,16,1362.6200000000001
MG,joao pinheiro,16,16,2475.31
MG,santana do paraiso,16,16,2696.8199999999997
MG,jacutinga,16,18,2670.82
MG,santa vitoria,16,17,4083.77
PB,patos,16,16,4036.65
SP,bom jesus dos perdoes,16,17,1608.73
PR,marialva,16,16,2573.17
SP,piraju,16,17,4659.09
MT,agua boa,16,18,2758.87
RO,vilhena,16,16,1973.95
PA,tucurui,16,16,4976.7
MS,ponta pora,16,18,4038.5099999999998
PE,salgueiro,16,17,2315.95
PA,paragominas,16,18,2033.65
RJ,itaocara,16,16,1720.65
GO,senador canedo,16,16,1375.57
RS,charqueadas,16,17,1721.41
SP,candido mota,16,16,1573.29
SP,ipero,16,18,2659.28
SP,santa adelia,15,15,1609.65
SP,novo horizonte,15,16,2588.4
MG,paraisopolis,15,15,2101.66
SP,barrinha,15,18,2965.14
SP,bariri,15,15,2706.45
RS,sao luiz gonzaga,15,15,3298.0099999999998
ES,guacui,15,16,3797.29
SC,barra velha,15,15,1684.01
SP,americo brasiliense,15,17,2360.1
SC,bombinhas,15,15,1935.4099999999999
MG,nova era,15,15,2074.71
MT,campo novo do parecis,15,15,4915.79
RS,palmeira das missoes,15,16,1559.51
MG,janauba,15,16,2952.26
RS,estrela,15,15,2113.2
PR,sao mateus do sul,15,15,1933.95
RJ,sao joao da barra,15,15,2115.54
GO,inhumas,15,16,2210.83
SP,pariquera-acu,15,15,1765.1
PR,jacarezinho,15,16,1289.36
SC,sao francisco do sul,15,16,1549.08
PE,vitoria de santo antao,15,15,2455.15
RJ,cantagalo,15,17,1981.48
SP,bastos,15,17,1399.6
RJ,pirai,15,15,2218.16
SP,taquarituba,15,15,2418.62
SC,penha,15,15,2092.39
PR,rio negro,15,15,2105.87
SP,osvaldo cruz,15,16,1786.46
GO,posse,15,15,3520.35
ES,venda nova do imigrante,15,15,2647.83
RS,nova prata,15,16,1230.94
SP,cordeiropolis,15,15,1260.05
RS,sao borja,15,18,2124.74
PE,ipojuca,14,15,1530.3
MG,esmeraldas,14,14,1780.97
PR,lapa,14,14,2039.2
SP,junqueiropolis,14,15,2029.24
SE,itabaiana,14,15,3125.77
RS,sao lourenco do sul,14,14,2135.38
SE,nossa senhora do socorro,14,14,2282.92
SP,santo anastacio,14,17,1884.6
SP,guariba,14,14,1608.43
MG,conselheiro pena,14,15,2000.56
GO,quirinopolis,14,14,1475.95
PR,piraquara,14,14,1604.51
ES,santa maria de jetiba,14,15,1888.97
SC,campos novos,14,14,1929.69
RJ,bom jardim,14,14,2189.4500000000003
MS,chapadao do sul,14,14,1569.79
SP,pirapora do bom jesus,14,16,2744.66
RS,frederico westphalen,14,14,1053.45
CE,iguatu,14,14,3538.29
SP,cunha,14,14,2845.12
SC,ituporanga,14,15,3225.16
GO,ipora,14,15,2025.99
MT,mirassol d'oeste,14,14,1912.02
MA,sao jose de ribamar,14,14,1444.82
MG,iturama,14,14,1655.55
MG,almenara,14,14,2872.15
SP,iguape,14,14,1359.5700000000002
RJ,sao francisco de itabapoana,14,15,1497.76
MG,santo antonio do monte,14,14,1909.12
RS,feliz,14,14,2523.43
SC,porto uniao,14,14,3023.65
RJ,natividade,13,15,2645.37
SP,jardinopolis,13,13,1600.05
MS,paranaiba,13,14,1396.24
MG,taiobeiras,13,13,2684.71
PR,loanda,13,13,1704.36
SP,miguelopolis,13,14,1984.27
MG,tupaciguara,13,13,1331.21
RJ,parati,13,13,2779.7
GO,porangatu,13,13,1828.15
SC,rio negrinho,13,13,1121.19
BA,serrinha,13,14,1889.1399999999999
RJ,barra de sao joao,13,13,2440.85
BA,santa maria da vitoria,13,13,1710.55
RS,eldorado do sul,13,15,1853.48
PA,marituba,13,14,1224.29
BA,pojuca,13,13,1481.09
ES,jaguare,13,13,1193.95
SC,taio,13,14,4366.23
RJ,pinheiral,13,14,2165.19
GO,novo gama,13,13,1777.05
MG,sao joao nepomuceno,13,14,2594.0
CE,eusebio,13,13,2217.51
ES,sao gabriel da palha,13,13,1406.8000000000002
MS,maracaju,13,13,2791.96
SP,pirapozinho,13,14,1319.3700000000001
MG,itanhandu,13,13,1830.08
SC,ibirama,13,13,1026.5
SC,fraiburgo,13,13,2028.57
SC,guaramirim,13,13,1377.08
PR,bandeirantes,13,13,1728.2
MG,divino,13,13,1208.59
SC,laguna,13,14,2202.73
SP,casa branca,13,13,1261.58
RS,lagoa vermelha,13,14,1616.25
SP,descalvado,13,13,1231.74
RS,imbe,13,13,2727.95
RS,ivoti,13,13,1235.1100000000001
SP,serra negra,13,13,3202.53
SP,aluminio,13,13,1252.15
SP,serrana,13,13,917.9
MG,buritis,13,13,1740.5700000000002
SP,sao lourenco da serra,12,12,1151.95
SP,teodoro sampaio,12,12,1259.77
SP,tabapua,12,12,1322.96
RO,ariquemes,12,13,4124.97
RO,cacoal,12,12,1801.47
SP,sao miguel arcanjo,12,13,1311.09
SP,vargem grande do sul,12,12,778.7
SP,sao pedro,12,12,3683.54
RS,flores da cunha,12,12,1439.45
MG,sacramento,12,13,1986.57
SP,pinhalzinho,12,12,1300.42
MG,itapecerica,12,13,1363.28
MG,abaete,12,12,1732.81
SP,cesario lange,12,13,1966.5
SP,chavantes,12,12,926.52
SP,engenheiro coelho,12,12,1049.48
SP,pilar do sul,12,12,1002.36
GO,ipameri,12,12,2100.55
BA,irece,12,13,1729.52
SP,jose bonifacio,12,12,1486.34
RS,camaqua,12,12,1693.85
PR,palmeira,12,12,2013.3200000000002
RJ,paty do alferes,12,13,2234.66
RS,rosario do sul,12,14,933.25
SP,salto de pirapora,12,12,970.59
RJ,mangaratiba,12,12,974.84
SP,lucelia,12,12,961.35
MG,bocaiuva,12,13,1618.27
SP,quata,12,12,3119.56
MG,tres marias,12,13,840.44
RS,santa vitoria do palmar,12,12,1750.75
RJ,mendes,12,12,1240.75
SP,mirandopolis,12,13,1274.99
CE,quixada,12,12,2620.67
PR,ibipora,12,12,1303.38
RJ,conceicao de macabu,12,12,1626.47
MG,matozinhos,12,12,750.65
MG,conceicao do mato dentro,12,12,1317.91
RJ,sao jose do vale do rio preto,12,12,1192.21
GO,morrinhos,12,14,1479.79
PA,redencao,12,12,1423.25
SP,pontal,12,12,1097.3799999999999
RJ,carmo,12,12,1415.19
MG,matias barbosa,12,13,2169.86
GO,niquelandia,12,13,1577.6699999999998
MG,sao francisco,12,12,1193.62
SP,brotas,12,12,1073.08
MA,santa ines,12,12,1226.88
RS,parobe,12,12,1750.48
RJ,aperibe,12,12,1464.94
PR,assis chateaubriand,12,12,1200.31
SC,forquilhinha,12,13,1143.85
SP,pirajui,12,12,1583.52
RS,tres de maio,12,12,1969.05
SP,macatuba,12,12,2984.64
MG,paraguacu,12,12,1452.85
RS,teutonia,12,14,1493.6000000000001
ES,anchieta,12,14,1983.8
RS,taquari,11,11,1619.28
ES,afonso claudio,11,11,1568.77
MA,bacabal,11,11,3243.71
MG,varzea da palma,11,11,2171.77
SP,aracoiaba da serra,11,11,1511.57
MS,nova andradina,11,11,2194.87
RS,cangucu,11,12,1310.18
PE,araripina,11,11,1070.58
PE,belo jardim,11,11,1578.63
SC,araquari,11,11,993.25
MA,presidente dutra,11,11,2000.98
RS,tres passos,11,11,1270.21
SP,santa rosa de viterbo,11,13,1658.42
SC,treze tilias,11,11,885.6600000000001
RS,triunfo,11,11,1918.53
PE,igarassu,11,11,1826.38
SC,santo amaro da imperatriz,11,11,2972.31
MG,mantena,11,11,1652.22
SP,tanabi,11,11,1404.39
MS,coxim,11,11,1598.75
PB,cajazeiras,11,11,1818.16
MG,raul soares,11,12,1115.51
SP,dois corregos,11,11,1233.69
SC,itapiranga,11,11,2667.18
MG,raposos,11,11,1009.52
MG,carandai,11,11,1143.5
PR,coronel vivida,11,11,856.87
MG,capinopolis,11,11,1042.18
PA,abaetetuba,11,11,4028.57
BA,candeias,11,12,1091.18
BA,itamaraju,11,11,1304.23
SP,tapiratiba,11,12,2601.2200000000003
SE,lagarto,11,11,1955.4299999999998
RS,sao sebastiao do cai,11,12,1588.84
SP,santa gertrudes,11,11,1194.21
SP,itaporanga,11,12,2237.28
MG,andradas,11,12,4070.31
RJ,goitacazes,11,11,1116.3400000000001
RJ,italva,11,12,1243.09
MS,costa rica,11,12,1043.66
GO,pires do rio,11,12,3500.83
MG,barroso,11,11,1289.96
SC,faxinal dos guedes,11,11,1512.73
SP,boa esperanca do sul,11,11,836.9
PE,santa cruz do capibaribe,11,11,2169.37
PE,sao lourenco da mata,11,11,1190.96
SP,ibate,11,12,1512.6
MG,pompeu,11,11,1055.18
SP,ouroeste,11,11,1235.19
PR,santo antonio da platina,11,12,1140.6100000000001
MS,rio brilhante,11,11,972.28
MG,alvinopolis,11,11,807.06
RS,encantado,11,11,2807.17
RJ,quissama,11,11,1513.97
SP,guararema,11,11,1189.56
PR,goioere,11,11,1935.28
MA,timon,11,11,1123.72
MT,canarana,10,10,1103.73
MT,nova xavantina,10,10,3274.69
PR,antonina,10,10,2077.57
SP,embu,10,11,1517.88
SP,fartura,10,10,1771.4099999999999
SP,castilho,10,10,2822.21
CE,brejo santo,10,10,1529.8600000000001
MG,prata,10,10,1044.58
SP,charqueada,10,10,1122.67
GO,goiatuba,10,10,2347.44
SP,paranapanema,10,11,560.45
MG,resplendor,10,10,739.0600000000001
RS,mostardas,10,11,1517.83
MG,aimores,10,10,951.37
RS,julio de castilhos,10,10,787.54
MG,corinto,10,11,1362.8600000000001
SP,paraibuna,10,10,1610.99
BA,campo formoso,10,10,3419.13
MT,querencia,10,10,2302.62
TO,paraiso do tocantins,10,10,1799.0400000000002
SP,taguai,10,10,707.34
MT,alta floresta,10,12,3495.55
SP,urupes,10,10,1150.14
BA,catu,10,10,1486.97
PR,sao joao,10,11,872.09
PR,cafelandia,10,11,1645.11
SP,palestina,10,10,499.55
RS,portao,10,10,772.15
GO,minacu,10,11,1561.6200000000001
RS,dom pedrito,10,10,1461.93
PB,guarabira,10,10,1239.68
SP,caconde,10,10,1628.19
SP,buri,10,10,938.3199999999999
SC,capinzal,10,10,1220.55
PR,palotina,10,10,872.76
SP,biritiba-mirim,10,10,1381.72
PE,serra talhada,10,10,2053.18
CE,limoeiro do norte,10,11,1156.67
GO,piracanjuba,10,10,1893.26
SC,sao joao batista,10,10,1675.22
GO,planaltina,10,10,754.24
SP,pradopolis,10,10,901.0
SP,itai,10,10,1757.58
SP,itajobi,10,10,1653.95
PR,paicandu,10,10,943.16
SP,auriflama,10,10,1871.6599999999999
SP,salesopolis,10,10,1146.52
SP,rio das pedras,10,10,1027.64
BA,caetite,10,10,1892.3
SP,regente feijo,10,10,897.01
SP,aguas da prata,10,10,1028.28
PE,escada,10,10,2658.43
BA,mata de sao joao,10,11,1083.55
PE,carpina,10,10,2194.76
SC,urussanga,10,10,893.6800000000001
PE,gravata,10,10,1806.19
MG,boa esperanca,10,11,1539.82
MG,carmo do cajuru,10,10,1638.44
PE,bezerros,10,10,1277.39
MG,eloi mendes,10,10,1795.3899999999999
RJ,papucaia,10,10,1126.77
CE,itapipoca,10,10,1121.08
RN,caico,10,10,2723.2
CE,taua,10,10,933.13
MT,campo verde,10,10,781.38
MG,campina verde,10,10,659.48
SP,taruma,9,9,997.72
MT,pontes e lacerda,9,9,1556.77
SP,sao simao,9,10,1297.8899999999999
SP,vera cruz,9,9,934.17
SP,lindoia,9,9,606.03
RS,serafina correa,9,9,813.66
PE,goiana,9,9,606.93
RS,tapejara,9,9,1165.13
RS,sao marcos,9,9,816.42
BA,itaberaba,9,9,989.26
SP,juquia,9,9,710.0799999999999
SP,monte aprazivel,9,10,948.11
PR,arapoti,9,9,966.97
PR,andira,9,11,1462.18
PR,campina grande do sul,9,9,1062.57
SC,herval d'oeste,9,9,1106.74
PR,cambara,9,9,803.1700000000001
PE,abreu e lima,9,11,2376.95
BA,santo amaro,9,10,1805.93
PE,petrolandia,9,9,1520.49
MG,guaranesia,9,9,805.5799999999999
MG,igarape,9,9,1734.47
PE,pesqueira,9,9,667.79
RS,rolante,9,9,874.25
GO,santa helena de goias,9,9,1499.73
SP,morro agudo,9,9,1670.95
RJ,sumidouro,9,10,1060.68
MG,aracuai,9,9,1362.98
SC,schroeder,9,9,1168.69
RS,girua,9,10,1335.28
SC,pinhalzinho,9,9,816.86
SC,pomerode,9,9,1579.36
CE,crateus,9,9,2407.76
SC,porto belo,9,9,856.3199999999999
PA,rondon do para,9,9,2780.13
SP,buritama,9,9,1024.24
SC,sao joaquim,9,9,1118.98
ES,santa teresa,9,10,1117.36
MG,mar de espanha,9,9,1014.72
SP,brodowski,9,9,935.54
GO,alto paraiso de goias,9,9,1367.3400000000001
SP,cajuru,9,9,643.76
MG,jequitinhonha,9,11,1372.3700000000001
RS,garibaldi,9,9,1014.8
PR,santa helena,9,9,628.15
PR,sao miguel do iguacu,9,9,1079.3
PR,faxinal,9,9,848.05
PR,siqueira campos,9,9,1478.08
MG,lagoa da prata,9,10,1685.69
SP,duartina,9,10,1252.67
SC,itapoa,9,9,849.67
PA,xinguara,9,9,1282.22
RS,itaqui,9,9,1154.38
SC,maravilha,9,9,497.17
SP,piquete,9,9,771.09
BA,conceicao do coite,9,9,997.89
MG,rio paranaiba,9,9,680.27
MG,itamonte,9,10,883.15
SP,santa branca,9,9,763.76
PA,canaa dos carajas,9,9,1565.93
PA,braganca,9,9,1083.96
AP,santana,9,9,1202.6399999999999
SE,estancia,9,9,2594.65
MG,paraopeba,9,9,880.67
SP,santa cruz das palmeiras,9,9,580.59
BA,bom jesus da lapa,9,9,2829.63
MG,nova ponte,9,9,1409.49
MG,camanducaia,9,9,2180.67
RN,pau dos ferros,9,9,2745.5499999999997
MS,sidrolandia,9,11,1557.76
CE,russas,9,9,3843.8700000000003
MG,nepomuceno,9,9,610.9399999999999
SP,aguai,9,9,1985.55
CE,tiangua,9,9,2377.09
SC,sombrio,9,10,1175.92
SC,sao lourenco do oeste,9,9,781.38
ES,mimoso do sul,9,9,687.37
SP,primavera,9,9,996.78
MG,passa quatro,9,9,1576.66
SC,xaxim,9,10,1718.58
MG,monte santo de minas,9,9,869.28
CE,morada nova,9,9,1295.28
PR,ibaiti,9,11,1057.3600000000001
PR,guaratuba,9,9,1821.8799999999999
SP,maracai,8,8,1114.58
SP,martinopolis,8,8,3708.09
MG,candeias,8,9,788.39
AL,palmeira dos indios,8,8,1094.41
BA,macaubas,8,8,867.47
MG,fervedouro,8,8,965.76
MG,ipaba,8,8,1403.5
BA,tucano,8,8,748.69
RJ,cambuci,8,8,2042.79
PE,afogados da ingazeira,8,8,1345.98
MG,sao goncalo do sapucai,8,8,1202.5
BA,ribeira do pombal,8,8,618.19
SP,icem,8,9,885.97
SP,guaicara,8,8,767.23
MG,sao jose da lapa,8,8,1086.58
MA,coroata,8,9,873.48
SP,nova europa,8,8,634.44
SP,jacare,8,8,810.0400000000001
PE,palmares,8,8,1206.82
MG,ibia,8,8,1367.29
SC,correia pinto,8,11,1454.23
MG,sao joaquim de bicas,8,8,1663.28
SC,balneario picarras,8,8,1426.81
PE,ouricuri,8,8,2246.86
MT,colider,8,8,2161.73
SP,angatuba,8,8,818.75
SP,valparaiso,8,8,506.92
AL,penedo,8,8,1239.8700000000001
SP,alvares machado,8,8,4022.57
TO,porto nacional,8,8,1577.68
MG,dores de campos,8,8,1308.1399999999999
MG,turmalina,8,8,1093.69
PA,sao felix do xingu,8,8,1382.7
SP,colina,8,9,608.68
CE,camocim,8,8,1686.29
GO,cidade ocidental,8,8,705.38
SC,itaiopolis,8,8,1313.5900000000001
MG,santa juliana,8,8,1723.3899999999999
MG,mateus leme,8,8,497.38
MG,arinos,8,8,752.0699999999999
SP,borborema,8,8,816.05
MG,poco fundo,8,8,933.99
PR,porecatu,8,9,735.42
PR,pontal do parana,8,8,1084.26
GO,anicuns,8,8,661.9300000000001
MG,piranguinho,8,9,1475.65
CE,ico,8,8,1990.88
RS,getulio vargas,8,8,746.61
SP,piratininga,8,8,1583.28
BA,cicero dantas,8,9,2974.15
GO,cristalina,8,8,2112.65
SP,cananeia,8,8,727.66
SC,papanduva,8,8,669.41
MG,lambari,8,8,1506.47
SP,cajobi,8,8,1018.4300000000001
SP,dourado,8,8,920.4300000000001
MG,rio acima,8,8,513.66
PR,capanema,8,9,602.59
SC,lauro muller,8,8,1449.57
RS,jaguarao,8,8,1025.29
GO,goias,8,8,1084.21
GO,goianira,8,8,853.8100000000001
GO,cacu,8,8,982.6800000000001
SC,orleans,8,8,1408.5900000000001
RS,nova petropolis,8,8,459.89
SP,pedro de toledo,8,8,733.22
MS,bonito,8,8,991.47
ES,pinheiros,8,8,1024.32
MG,perdizes,8,8,1163.31
RS,encruzilhada do sul,8,8,903.99
ES,joao neiva,8,8,724.9300000000001
PR,nova londrina,8,9,743.53
MG,muzambinho,8,9,665.8
MG,mutum,8,8,1397.94
PR,nova esperanca,8,8,1579.78
ES,ecoporanga,8,8,881.9200000000001
MG,perdoes,8,9,603.88
ES,domingos martins,8,9,1188.3
MG,mirai,8,8,841.8100000000001
PR,ortigueira,8,8,993.29
MS,navirai,8,8,1910.88
RJ,trajano de moraes,8,8,775.1800000000001
SP,potirendaba,8,8,707.32
ES,marilandia,8,8,1436.07
ES,barra de sao francisco,8,9,627.56
MG,astolfo dutra,8,11,1294.52
PR,mambore,8,8,780.24
PR,mangueirinha,8,8,1524.77
PR,jandaia do sul,8,8,1839.25
ES,baixo guandu,8,8,1399.1
ES,ibatiba,8,9,1518.78
MG,baependi,8,8,1409.04
MG,carmo do rio claro,8,9,1642.42
MG,bom jardim de minas,8,8,866.87
MG,caetanopolis,8,8,664.5699999999999
MG,botelhos,8,8,1240.01
MG,brasilia de minas,8,9,671.74
RS,arroio do meio,8,9,1400.22
RS,arroio dos ratos,8,9,1034.18
MG,buritizeiro,8,8,2611.19
MT,aripuana,8,8,1124.78
MT,sapezal,8,8,964.82
AL,teotonio vilela,7,7,2043.88
MS,sao gabriel do oeste,7,7,526.72
SP,sao bento do sapucai,7,7,630.54
MT,confresa,7,7,1065.6499999999999
TO,dianopolis,7,7,822.9499999999999
CE,acopiara,7,7,647.67
GO,campinorte,7,7,1244.69
SC,passo de torres,7,7,587.99
GO,ceres,7,7,1905.47
BA,morro do chapeu,7,7,557.57
BA,mucuri,7,7,2203.67
PE,limoeiro,7,7,511.59
MG,simonesia,7,8,1295.88
SP,itapui,7,7,1307.09
BA,nucleo residencial pilar,7,8,2024.35
MG,lagoa formosa,7,7,647.5699999999999
CE,cruz,7,7,1480.58
SP,conchas,7,8,1064.45
PR,cruzeiro do oeste,7,7,825.39
PA,conceicao do araguaia,7,7,1143.8899999999999
RS,casca,7,7,1326.27
RN,alto do rodrigues,7,8,2737.46
RN,currais novos,7,7,1448.19
MG,pirapetinga,7,7,486.39
BA,camamu,7,8,1411.82
SP,pirangi,7,7,1055.0900000000001
RS,cerro largo,7,7,712.87
MG,arceburgo,7,7,924.14
ES,sao domingos do norte,7,7,874.4000000000001
PR,prudentopolis,7,7,839.09
MG,malacacheta,7,7,1355.65
PR,quedas do iguacu,7,8,842.25
SC,rodeio,7,7,849.66
SP,itabera,7,7,1366.14
SP,luis antonio,7,7,980.08
PE,catende,7,7,1630.1799999999998
GO,bom jesus,7,8,928.27
GO,campos belos,7,7,788.0699999999999
BA,madre de deus,7,7,633.32
GO,chapadao do ceu,7,8,1108.57
MG,itamarandiba,7,8,1706.99
BA,potiragua,7,7,495.97
ES,montanha,7,10,1586.54
RS,horizontina,7,7,576.54
SP,cafelandia,7,8,729.2
PR,guaira,7,7,820.48
PR,imbituva,7,8,740.6700000000001
RJ,vila muriqui,7,7,731.76
MA,sao joao dos patos,7,7,1333.08
RS,espumoso,7,7,1210.71
PR,pinhao,7,8,920.28
ES,vila valerio,7,8,1369.4
GO,acreuna,7,7,1070.43
GO,jaragua,7,7,610.67
GO,neropolis,7,7,1297.22
SC,campo ere,7,7,560.6
PR,terra rica,7,7,644.6700000000001
PR,ubirata,7,7,582.1800000000001
BA,inhambupe,7,7,1117.78
BA,ipiau,7,7,697.27
MG,piedade de caratinga,7,7,662.07
PR,ivaipora,7,7,516.75
SP,avanhandava,7,7,757.6800000000001
RJ,santa maria madalena,7,7,1046.09
MG,cristina,7,7,1009.42
RJ,areal,7,7,1152.18
MG,inhapim,7,7,436.35
MG,ipanema,7,7,3727.77
BA,itacare,7,7,808.1899999999999
SP,igarapava,7,7,791.09
BA,ruy barbosa,7,7,662.96
SP,ipaussu,7,7,1228.72
PE,timbauba,7,7,567.67
ES,itaguacu,7,7,1758.0300000000002
GO,silvania,7,7,1208.79
SP,morungaba,7,7,582.6899999999999
SP,nhandeara,7,7,595.26
BA,ibotirama,7,7,3032.39
SP,guara,7,7,842.8
CE,nova russas,7,7,1504.94
SP,aracariguama,7,8,616.88
PB,bayeux,7,7,808.05
PE,bom conselho,7,7,1624.93
GO,santa rita do araguaia,7,7,800.25
MA,barra do corda,7,7,889.89
RS,xangri-la,7,8,1013.58
RJ,comendador levy gasparian,7,7,603.6899999999999
GO,sao luis de montes belos,7,7,1196.3700000000001
SE,sao cristovao,7,7,618.69
RJ,porciuncula,7,8,936.8800000000001
RS,sao jeronimo,7,7,569.75
RS,sao jose do norte,7,7,548.5
RS,santo augusto,7,8,1115.08
RS,santo cristo,7,7,609.45
MG,santo antonio do jacinto,7,7,406.59
PR,missal,7,7,2490.76
PI,campo maior,7,7,993.6600000000001
PI,cocal,7,7,896.77
MG,ervalia,7,7,1076.83
MA,codo,7,7,2224.82
GO,rubiataba,7,7,1034.0900000000001
MA,acailandia,7,7,937.79
PI,piripiri,7,7,537.28
PI,sao raimundo nonato,7,7,2145.39
PR,marmeleiro,7,7,698.44
SE,simao dias,7,7,828.48
MA,paco do lumiar,7,7,766.38
MS,aparecida do taboado,7,7,2531.9
PB,sousa,7,7,1042.59
BA,arraial d'ajuda,7,7,594.42
RO,pimenta bueno,7,7,1243.79
RO,rolim de moura,7,7,465.04999999999995
TO,tocantinopolis,7,7,731.65
GO,crixas,7,8,893.68
GO,bela vista de goias,7,7,608.66
SP,ribeirao bonito,7,7,727.29
MG,campanha,7,7,598.79
RN,sao goncalo do amarante,7,7,859.78
SP,santa albertina,7,7,686.39
BA,vera cruz,7,7,1243.52
PR,ceu azul,7,7,382.56
SP,divinolandia,7,7,1370.68
PR,carlopolis,6,6,755.4
SP,sales oliveira,6,6,538.15
MG,borda da mata,6,6,897.53
RS,bom principio,6,6,1003.11
MG,carai,6,6,481.87
RO,espigao do oeste,6,6,706.6800000000001
MG,bicas,6,7,727.65
RS,campinas do sul,6,6,1398.89
MG,cassia,6,6,278.29
SC,nova trento,6,6,870.6
SP,tupi paulista,6,6,459.40999999999997
MT,comodoro,6,7,2245.02
MG,cachoeira de minas,6,6,454.5
RS,balneario pinhal,6,7,898.57
RO,jaru,6,6,660.59
RS,butia,6,6,1112.69
MG,brazopolis,6,6,856.13
BA,barra da estiva,6,7,860.57
CE,acarau,6,8,1364.96
MS,amambai,6,6,751.98
SP,pacaembu,6,6,1505.29
BA,ipira,6,6,3232.78
SP,iacanga,6,6,329.39
ES,boa esperanca,6,7,1097.58
MG,novo cruzeiro,6,9,805.78
PI,regeneracao,6,6,790.97
PI,oeiras,6,6,553.44
MG,guarani,6,7,2164.42
RS,tres coroas,6,6,774.37
RS,tres cachoeiras,6,7,646.27
RS,tapes,6,6,797.3499999999999
MG,espinosa,6,6,2705.09
MG,entre rios de minas,6,7,1503.86
MG,fronteira,6,6,949.6600000000001
MG,sao goncalo do rio abaixo,6,6,802.2
ES,apiaca,6,6,434.28
ES,alfredo chaves,6,7,902.71
SP,guapiacu,6,6,906.98
PR,ampere,6,8,1595.27
SP,ibira,6,6,739.83
MG,dores do indaia,6,7,744.57
RS,sao sepe,6,6,544.35
RJ,porto real,6,7,1484.6
RS,sananduva,6,6,453.77
RS,ronda alta,6,6,1544.3300000000002
SC,apiuna,6,7,1320.6
SP,monte alegre do sul,6,6,4181.79
RJ,engenheiro paulo de frontin,6,6,449.12
RJ,cardoso moreira,6,6,500.02
GO,orizona,6,6,546.8100000000001
SC,catanduvas,6,6,690.79
SC,abelardo luz,6,6,679.6999999999999
SC,benedito novo,6,6,945.74
GO,itapuranga,6,6,800.8800000000001
PE,cabrobo,6,6,921.79
PE,aguas belas,6,6,769.87
MG,virginopolis,6,7,614.64
PB,mamanguape,6,6,969.75
PB,esperanca,6,6,1720.38
PB,catole do rocha,6,6,3742.59
PB,cabedelo,6,6,888.95
MS,camapua,6,6,621.29
BA,entre rios,6,6,1103.4
SP,parapua,6,8,1178.4
CE,quixeramobim,6,6,859.79
SP,apiai,6,6,547.5699999999999
PR,mallet,6,6,786.65
CE,pacajus,6,6,1262.59
SP,nazare paulista,6,7,815.64
PR,nova prata do iguacu,6,6,1049.78
SC,gravatal,6,6,1260.27
RJ,santo amaro de campos,6,6,1611.78
RJ,rio das flores,6,6,558.68
BA,coribe,6,8,654.97
PA,uruara,6,6,962.4
SP,bady bassitt,6,6,517.8
SP,bilac,6,7,680.62
SP,fernando prestes,6,6,591.48
PR,astorga,6,7,411.77
BA,seabra,6,6,982.5
GO,guapo,6,6,757.89
SC,ipora do oeste,6,6,509.85
GO,mozarlandia,6,7,806.4
RJ,california da barra,6,6,871.97
ES,rio novo do sul,6,6,531.68
PR,pirai do sul,6,6,601.29
MG,medina,6,6,579.19
MG,mata verde,6,6,1512.53
MG,alpinopolis,6,7,836.6800000000001
MG,areado,6,6,1246.69
RJ,tangua,6,6,504.88
BA,trancoso,6,6,754.2
CE,itapaje,6,6,3198.6800000000003
PR,itapejara d'oeste,6,6,1049.9
PR,itaipulandia,6,6,195.17
SP,cabreuva,6,6,720.6
RS,nao-me-toque,6,7,859.68
PR,pinhalao,6,7,1894.94
MG,sao jose da barra,6,6,987.14
MG,sao joao evangelista,6,6,1062.76
MG,itaobim,6,6,866.9100000000001
MG,itambacuri,6,6,601.77
GO,itaberai,6,6,1012.08
BA,medeiros neto,6,7,660.24
MG,tocantins,6,6,681.38
MG,teixeiras,6,6,483.58
BA,jeremoabo,6,6,922.0799999999999
SC,morro da fumaca,6,7,1676.0
GO,cachoeira alta,6,6,451.76
SP,itobi,6,7,472.68
SP,irapuru,6,6,889.48
PR,primeiro de maio,6,7,1216.67
ES,sao jose do calcado,6,6,970.18
PR,rio branco do sul,6,6,418.57
BA,canavieiras,6,6,799.8
BA,camacan,6,6,1134.67
PA,santa isabel do para,6,6,741.77
PA,pacaja,6,6,2651.06
CE,caninde,6,6,645.38
SP,cedral,6,6,458.34000000000003
SP,catigua,6,6,668.57
BA,ubaira,6,6,704.79
MG,rio pomba,6,6,1192.8600000000001
MG,santa rita de caldas,6,6,746.28
SP,general salgado,6,6,493.59
MG,carmo da mata,6,6,459.7
PA,jacunda,6,6,1601.71
PA,barcarena,6,6,1084.17
BA,valente,6,9,3209.58
SP,cardoso,6,6,944.8100000000001
PR,colorado,6,6,1022.78
CE,barbalha,6,6,1302.98
SP,cosmorama,6,6,973.98
CE,hidrolandia,6,7,953.77
SP,itariri,6,6,1259.32
SP,itapura,6,6,351.87
PE,lajedo,6,6,916.27
PR,reboucas,6,6,361.27
PR,realeza,6,6,1264.26
SC,presidente getulio,6,6,654.1800000000001
MT,campos de julio,6,6,934.8
AL,rio largo,6,6,562.71
TO,lagoa da confusao,5,5,699.99
SP,taiuva,5,5,881.54
MT,alto araguaia,5,5,1085.73
BA,andorinha,5,5,691.1
SP,roseira,5,5,423.68
MG,cambuquira,5,5,340.76
SP,tres fronteiras,5,5,350.39
AL,maragogi,5,5,1897.05
SP,severinia,5,5,466.13
SP,sud mennucci,5,5,377.87
SP,tabatinga,5,5,389.69
RS,arroio do sal,5,7,918.97
MT,itauba,5,5,1420.98
MT,jauru,5,5,613.79
MT,juara,5,5,378.49
MT,matupa,5,7,871.1700000000001
MT,nova mutum,5,5,571.38
MG,lima duarte,5,6,764.88
MG,jesuania,5,5,327.98
SC,otacilio costa,5,5,913.29
SC,palmitos,5,5,667.9
SC,piratuba,5,5,941.48
GO,alexania,5,5,466.67
PR,ribeirao claro,5,5,492.69
PR,ribeirao do pinhal,5,5,328.0
MG,serra dos aimores,5,5,351.82
PE,moreno,5,5,763.5
BA,paramirim,5,5,407.67999999999995
PR,santa fe,5,5,877.8
MG,lagoa dourada,5,5,586.78
PR,rio azul,5,5,383.70000000000005
PR,quatigua,5,5,251.7
SC,sao carlos,5,5,500.38
ES,sao roque do canaa,5,5,348.0
ES,sooretama,5,5,317.35999999999996
ES,vargem alta,5,5,278.89
BA,livramento de nossa senhora,5,5,655.54
PE,custodia,5,5,584.88
PE,floresta,5,6,454.58000000000004
SP,jacupiranga,5,5,785.8
MG,jordania,5,5,886.25
MG,juruaia,5,6,380.78000000000003
PR,senges,5,5,487.39
MG,jaiba,5,6,683.49
SC,laurentino,5,5,782.41
MG,soledade de minas,5,5,309.94
BA,miguel calmon,5,5,616.64
GO,firminopolis,5,7,613.49
MG,jeceaba,5,6,544.23
MG,itapagipe,5,5,265.49
MG,itau de minas,5,5,364.45
BA,prado,5,5,1090.79
MG,sao tiago,5,5,499.27
ES,pedro canario,5,5,363.79
MG,martins soares,5,6,408.79
SC,ipumirim,5,5,281.41
SC,garuva,5,5,1467.38
SP,iepe,5,5,289.58
SP,igarata,5,5,764.0899999999999
BA,remanso,5,5,369.69
MG,sao romao,5,5,388.49
PE,sirinhaem,5,5,571.88
PE,surubim,5,5,546.87
PE,tabira,5,5,986.88
PE,taquaritinga do norte,5,6,2064.91
MG,mendes pimentel,5,5,372.69
MG,monte azul,5,5,619.9
SP,ocaucu,5,5,241.6
PE,arcoverde,5,5,515.8
PE,barreiros,5,5,1302.1599999999999
PE,bonito,5,5,1235.79
SP,miracatu,5,5,863.99
BA,iraquara,5,5,390.8
SC,guabiruba,5,5,688.78
SC,anita garibaldi,5,5,256.78
SC,capivari de baixo,5,5,876.89
RJ,carapebus,5,5,696.97
GO,santo antonio do descoberto,5,5,866.26
GO,sao miguel do araguaia,5,5,1321.15
MG,monte belo,5,5,1109.78
SC,seara,5,5,582.87
ES,marechal floriano,5,5,559.64
SC,vargem bonita,5,5,710.59
ES,conceicao do castelo,5,5,507.83000000000004
SC,tres barras,5,5,297.34000000000003
ES,iconha,5,5,315.74
PE,toritama,5,5,1072.79
PI,altos,5,5,1345.39
MG,eugenopolis,5,5,973.87
RS,soledade,5,5,568.79
RS,terra de areia,5,5,1137.29
RS,sao francisco de paula,5,5,520.79
MA,alto parnaiba,5,5,777.79
PI,sao joao do piaui,5,5,1541.8000000000002
CE,santa quiteria,5,5,849.67
CE,sao goncalo do amarante,5,5,420.77
SP,adolfo,5,5,373.8
SP,holambra ii,5,5,919.68
BA,santa cruz cabralia,5,5,515.88
BA,santo estevao,5,5,979.81
SP,orindiuva,5,5,541.78
SP,palmeira d'oeste,5,5,319.18
PB,pombal,5,6,1577.5
PB,queimadas,5,5,1422.9
PB,santa luzia,5,5,285.3
PB,santa rita,5,6,1401.75
MG,vazante,5,6,1549.63
MG,frei inocencio,5,5,644.29
MA,lago da pedra,5,5,840.3699999999999
RJ,quatis,5,5,483.69
RS,nova santa rita,5,5,954.78
RS,sao jose do ouro,5,5,411.38000000000005
RS,sarandi,5,5,177.39000000000001
MG,divinolandia de minas,5,5,219.59
SP,ibirarema,5,5,426.88
CE,pacatuba,5,5,4317.98
MG,pedra azul,5,5,416.12
SP,ariranha,5,5,531.49
SP,guaranta,5,5,569.29
SP,panorama,5,5,404.39
SP,paulo de faria,5,5,588.5799999999999
BA,esplanada,5,5,1660.9
MS,cassilandia,5,5,1524.5
RS,rio pardo,5,5,687.88
BA,sao sebastiao do passe,5,5,399.89
SP,guarei,5,5,1098.29
PR,assai,5,5,861.5699999999999
PR,bituruna,5,5,433.38
BA,sobradinho,5,5,592.69
SP,bocaina,5,6,1391.9
SP,bofete,5,5,617.59
PR,japura,5,5,408.5
PB,bananeiras,5,5,295.24
MS,bataguassu,5,5,613.0
BA,euclides da cunha,5,5,524.1800000000001
BA,ibicarai,5,5,424.88
RS,pinheiro machado,5,5,542.89
RS,porto xavier,5,5,564.46
MA,viana,5,5,622.97
MG,aguas formosas,5,5,1341.7
SP,balsamo,5,6,1257.23
SP,bananal,5,5,582.25
CE,horizonte,5,5,519.99
CE,icapui,5,5,454.25
PR,guaraniacu,5,5,385.96999999999997
PR,inacio martins,5,5,242.99
SP,brauna,5,5,400.79
CE,jaguaribe,5,5,663.98
RS,estacao,5,5,704.1
MA,ze doca,5,5,688.5999999999999
MG,abre campo,5,5,281.68
MG,conceicao da aparecida,5,5,866.08
MG,conceicao do rio verde,5,5,825.89
MG,conquista,5,6,453.88
RS,dom feliciano,5,5,452.05
MG,belo oriente,5,5,620.39
BA,casa nova,5,6,1126.19
PA,sao miguel do guama,5,5,1240.79
MG,rio pardo de minas,5,5,597.69
MG,sabinopolis,5,5,317.08000000000004
SP,eldorado,5,5,504.77
SP,elias fausto,5,5,396.4
SP,estiva gerbi,5,7,964.26
CE,cascavel,5,5,1035.6599999999999
PR,floresta,5,5,729.79
PR,general carneiro,5,5,401.48
PA,novo progresso,5,5,2219.01
PA,ourilandia do norte,5,5,1710.0800000000002
PA,quatro bocas,5,5,1486.99
SP,presidente bernardes,5,5,466.86
BA,capim grosso,5,5,547.89
RS,cidreira,5,5,656.12
MG,arapora,5,5,1144.38
MG,araujos,5,5,2490.5
CE,granja,5,5,460.68
SP,colombia,5,5,377.72
PR,cidade gaucha,5,5,798.39
PR,colonia vitoria,5,5,294.90999999999997
PR,diamante do norte,5,5,391.25
MG,porteirinha,5,5,282.69
MG,presidente olegario,5,6,412.90999999999997
PA,dom eliseu,5,5,343.87
BA,cansancao,5,7,766.96
MG,catas altas,5,5,1052.85
MG,carmopolis de minas,5,5,1629.78
RS,cacapava do sul,5,5,859.99
SP,rafard,5,5,556.4
MG,campos altos,5,5,373.68
RN,macaiba,5,5,574.4399999999999
RN,macau,5,5,998.88
MG,capitolio,5,5,386.89
MG,caldas,5,5,489.7
RS,barra do ribeiro,5,5,553.78
SP,sales,5,5,356.52
PR,capitao leonidas marques,5,5,407.78
MG,rio casca,5,5,317.43
MG,rio manso,5,5,815.5600000000001
MT,guaranta do norte,5,5,393.87
SP,tarabai,5,5,982.35
SP,torrinha,5,6,422.67
TO,alvorada,5,6,1494.47
TO,araguatins,4,5,681.98
MT,peixoto de azevedo,4,4,357.7
RS,antonio prado,4,5,554.2
MG,bom jesus do galho,4,4,4795.289999999999
MG,bom repouso,4,4,402.29
MG,bom sucesso,4,4,856.6899999999999
RN,parelhas,4,4,1233.8899999999999
RN,santa cruz,4,4,522.74
SP,saltinho,4,5,1164.79
SP,santa barbara d oeste,4,4,170.92000000000002
MT,araputanga,4,4,517.45
PA,cameta,4,4,392.8
PA,carajas,4,4,483.22
MS,ladario,4,4,292.69
MS,miranda,4,4,273.8
SP,quintana,4,4,353.0
RS,candiota,4,4,802.7
RS,capao do leao,4,4,1072.25
MG,pecanha,4,4,794.8
CE,ipu,4,4,379.88
PR,indianopolis,4,4,262.79
SP,cabralia paulista,4,4,207.29
MG,santa maria de itabira,4,4,462.3
MG,rio piracicaba,4,4,512.75
MG,rio preto,4,4,161.68
BA,ubaitaba,4,4,517.23
BA,uibai,4,4,549.98
BA,una,4,4,437.88
CE,campos sales,4,4,1543.9
PR,figueira,4,4,928.78
MG,piranga,4,4,316.19
CE,forquilha,4,4,348.47
CE,jijoca de jericoacoara,4,4,1130.9
CE,guaraciaba do norte,4,4,605.15
PR,mandaguacu,4,4,3222.0
MG,palma,4,4,415.89
SP,altinopolis,4,4,1428.8
SP,analandia,4,4,511.03
BA,serra do ramalho,4,4,317.09000000000003
PR,araruna,4,4,429.97
PR,boa vista da aparecida,4,4,202.47
MG,santa cruz de minas,4,5,578.89
SP,florida paulista,4,4,353.79
BA,tanhacu,4,4,528.78
BA,teolandia,4,4,167.8
CE,jaguaruana,4,4,1155.15
SP,bernardino de campos,4,4,256.09000000000003
PR,itaperucu,4,4,635.84
MG,perdigao,4,6,284.5
PR,jesuitas,4,4,556.5500000000001
CE,senador pompeu,4,4,585.94
PR,manoel ribas,4,4,631.65
ES,bom jesus do norte,4,4,699.89
CE,varjota,4,4,748.97
ES,agua doce do norte,4,4,365.48
ES,fundao,4,4,352.8
SE,poco verde,4,4,447.79999999999995
MG,sao domingos do prata,4,4,337.89
MG,sao geraldo,4,4,423.78
MG,santana da vargem,4,4,269.95
MG,santana do jacare,4,4,1685.79
MG,santo antonio do amparo,4,4,376.71999999999997
SP,guaracai,4,5,541.49
CE,morrinhos,4,4,917.8
CE,paracuru,4,4,550.89
CE,paraipaba,4,5,558.97
ES,arace,4,4,413.4
PR,munhoz de melo,4,4,953.89
PR,nova fatima,4,4,254.89
MG,munhoz,4,4,384.66999999999996
ES,mantenopolis,4,4,423.78999999999996
ES,dores do rio preto,4,4,411.76
SC,trombudo central,4,4,182.89
SC,turvo,4,4,194.89
PE,trindade,4,4,4084.8
PI,corrente,4,4,1489.9
PI,esperantina,4,4,414.65999999999997
PI,guadalupe,4,4,1313.7
PI,urucui,4,4,638.97
PI,valenca do piaui,4,4,1043.0
CE,santana do acarau,4,4,1376.8899999999999
CE,sao benedito,4,4,789.19
PR,peabiru,4,4,675.39
PR,pien,4,4,330.4
ES,rio bananal,4,4,225.26
SP,igaracu do tiete,4,4,107.69
BA,riachao do jacuipe,4,5,2502.4
BA,riacho de santana,4,4,1194.7
PE,sertania,4,4,343.29
ES,itaipava,4,4,406.84
ES,itapemirim,4,4,372.70000000000005
PR,nova santa rosa,4,4,398.88
MG,merces,4,4,219.76
MG,minas novas,4,4,433.77
MG,monte alegre de minas,4,4,213.68
SC,sao jose do cedro,4,5,486.59000000000003
SC,saudades,4,4,305.84
SC,sideropolis,4,4,299.70000000000005
PR,rio bonito do iguacu,4,4,462.8
PR,planalto,4,4,353.7
MG,maravilhas,4,4,420.81
SC,salto veloso,4,4,418.8
SC,santa cecilia,4,4,505.79
SP,irapua,4,4,198.8
BA,piritiba,4,5,387.79
BA,posto da mata,4,4,530.98
BA,presidente tancredo neves,4,4,234.68
BA,queimadas,4,4,834.4499999999999
MG,sapucai-mirim,4,4,569.79
PE,sao bento do una,4,4,1328.3899999999999
PE,sao jose do egito,4,4,444.70000000000005
MG,sao joao do paraiso,4,4,349.5
ES,muqui,4,4,485.48
PR,paulo frontin,4,5,560.9
MG,jacui,4,4,403.74
GO,castelandia,4,5,554.98
SP,jambeiro,4,4,329.26
PE,parnamirim,4,4,1884.22
PE,ribeirao,4,4,316.4
SP,ipua,4,4,2031.49
PR,salto do lontra,4,4,766.49
PR,santa cruz de monte castelo,4,4,706.22
MG,lagoa grande,4,4,2060.89
PR,santa mariana,4,4,311.25
GO,corumbaiba,4,4,176.8
SC,palma sola,4,4,938.8
SC,praia grande,4,4,452.74
SC,quilombo,4,4,174.78
SC,rio do campo,4,4,674.95
PR,renascenca,4,4,279.6
MG,itanhomi,4,4,308.55
MG,itapeva,4,5,275.7
PR,terra boa,4,4,683.79
BA,mutuipe,4,4,448.78999999999996
SP,joanopolis,4,6,824.6
PE,condado,4,4,944.8
PE,feira nova,4,5,480.78
PE,gameleira,4,4,1657.98
PE,ilha de itamaraca,4,4,524.44
PE,joaquim nabuco,4,4,234.87
BA,pilao arcado,4,4,279.87
SP,itatinga,4,4,1760.15
GO,caiaponia,4,4,352.78
MG,juatuba,4,4,607.9
PR,saudade do iguacu,4,4,263.79
PR,sertanopolis,4,4,918.8
SC,imbuia,4,4,1501.88
SC,irineopolis,4,4,212.82
PR,tibagi,4,4,293.77
RJ,avelar,4,4,606.0
SP,macedonia,4,4,334.21
SP,maristela,4,4,639.3199999999999
SP,mendonca,4,4,230.37
MG,tarumirim,4,4,775.49
MG,tiradentes,4,4,510.86
MG,tombos,4,4,344.79
BA,maracas,4,5,703.64
SP,lavinia,4,4,326.8
GO,edeia,4,4,472.9
GO,fazenda nova,4,4,319.78999999999996
GO,goianapolis,4,4,1086.98
SC,jacinto machado,4,4,260.49
RJ,conservatoria,4,4,864.09
MG,gouveia,4,4,936.96
PE,brejo da madre de deus,4,4,410.8
BA,itiuba,4,4,272.89
BA,itabela,4,4,423.89
SC,guaruja do sul,4,4,331.44
GO,joviania,4,5,376.96999999999997
MG,guimarania,4,4,523.9
MG,iapu,4,4,383.15000000000003
SC,cocal do sul,4,4,2015.29
SC,corupa,4,4,434.65
SC,cunha pora,4,5,645.4200000000001
GO,maurilandia,4,4,265.63
SC,canelinha,4,4,933.94
SC,ibiam,4,4,382.99
SC,ilhota,4,4,749.1400000000001
MA,itapecuru mirim,4,4,552.97
MA,nova olinda do maranhao,4,4,1546.4
BA,gandu,4,4,417.7
MG,volta grande,4,4,308.38
MS,alcinopolis,4,6,711.1600000000001
SC,ascurra,4,4,342.6
RJ,japuiba,4,5,1017.58
GO,pirenopolis,4,4,273.87
GO,rianapolis,4,4,451.68
RJ,governador portela,4,4,349.8
SC,balneario arroio do silva,4,4,379.88
SC,balneario barra do sul,4,4,393.3
MA,barreirinhas,4,4,361.42
GO,nova veneza,4,4,339.95
GO,padre bernardo,4,4,195.7
GO,parauna,4,4,556.88
MA,urbano santos,4,5,501.79
RS,nova bassano,4,4,387.24
MG,aiuruoca,4,4,281.09000000000003
SP,paraiso,4,5,770.78
MA,pinheiro,4,4,426.8
RS,quarai,4,4,2402.99
RS,roque gonzales,4,5,542.88
RS,salto do jacui,4,4,196.36
MA,joao lisboa,4,5,612.89
MA,maracacume,4,4,617.18
MG,cruzilia,4,4,377.9
RS,palmares do sul,4,5,435.77
MA,buriticupu,4,4,585.78
MG,dom silverio,4,4,392.24
RS,santo antonio das missoes,4,4,393.89
MA,grajau,4,5,652.79
MG,bonfim,4,4,229.84
MG,conceicao das pedras,4,4,313.59000000000003
MG,conceicao dos ouros,4,4,632.78
MG,congonhal,4,4,455.84000000000003
MG,alto rio doce,4,4,213.42
BA,coaraci,4,4,1201.8799999999999
MS,fatima do sul,4,4,1436.29
MS,juti,4,4,631.79
PA,tailandia,4,4,2113.18
PA,vila dos cabanos,4,4,451.23
MS,caarapo,4,4,1310.49
SP,pedrinhas paulista,4,4,420.87
BA,iacu,4,4,340.7
RS,palmitinho,4,5,271.69
RS,pejucara,4,4,699.65
RJ,santanesia,4,4,364.5
RS,catuipe,4,4,539.8
MG,chapada gaucha,4,4,391.69
RN,jucurutu,4,4,632.98
MG,carmo da cachoeira,4,4,319.44
RS,candelaria,4,4,573.39
BA,cachoeira,4,4,479.79
PA,moju,4,4,242.88
SP,pongai,4,4,343.8
RS,chapada,4,4,1463.19
RS,chui,4,5,818.6999999999999
RS,condor,4,4,216.8
RJ,sao sebastiao do alto,4,4,488.98
RJ,sapucaia,4,4,548.75
RJ,silva jardim,4,4,567.5899999999999
RJ,travessao,4,4,414.09000000000003
RJ,varre-sai,4,4,918.9
MT,pedra preta,4,4,539.89
TO,guarai,4,4,1156.6
SP,sao sebastiao da grama,4,4,1024.79
AM,humaita,4,4,285.85
MT,claudia,4,4,302.68
MT,cocalinho,4,4,418.87
SP,santo antonio do jardim,4,4,231.03
BA,alcobaca,4,4,1289.78
SP,rosana,4,4,236.6
MG,bueno brandao,4,4,172.02
MG,buenopolis,4,4,1231.38
RO,ouro preto do oeste,4,4,437.49
MG,campo do meio,4,4,251.69
MG,campos gerais,4,4,457.16
MG,canapolis,4,5,525.8
RS,anta gorda,4,4,577.7
CE,barro,4,4,621.89
CE,bela cruz,4,4,899.9
PR,curiuva,4,4,295.70000000000005
PR,eneas marques,4,4,151.68
PR,candido de abreu,4,4,360.8
PR,centenario do sul,4,4,369.13
PR,chopinzinho,4,4,142.38
MG,rio novo,4,4,536.79
SP,cristais paulista,4,4,543.78
SP,clementina,4,4,397.54
AL,delmiro gouveia,4,4,1125.8
MT,diamantino,4,7,386.49
MT,chapada dos guimaraes,4,4,754.8
SP,sete barras,4,4,229.69
MT,nova bandeirantes,4,4,548.51
MT,paranaita,4,4,1858.75
TO,cristalandia,3,3,948.69
TO,conceicao do tocantins,3,3,367.97
TO,colinas do tocantins,3,3,510.5
MT,juruena,3,3,319.9
MT,jaciara,3,3,185.7
TO,xambioa,3,3,333.67999999999995
TO,taguatinga,3,3,355.79
SP,vista alegre do alto,3,3,272.99
SP,valentim gentil,3,3,372.03000000000003
SP,urania,3,4,885.72
SP,uchoa,3,3,582.64
SP,timburi,3,3,343.3
SP,taquarivai,3,3,674.89
AL,santana do mundau,3,3,1052.8
AL,pilar,3,3,99.7
SP,silveiras,3,3,406.50000000000006
SP,sao luis do paraitinga,3,3,882.49
SP,sao jose da bela vista,3,3,310.84000000000003
MT,colniza,3,3,718.97
MT,novo sao joaquim,3,3,292.6
MT,nova monte verde,3,3,245.79
MT,nova canaa do norte,3,3,149.77999999999997
BA,amelia rodrigues,3,3,372.39
SP,sao joao de iracema,3,3,168.38
SP,santo antonio da alegria,3,3,206.79000000000002
BA,araci,3,3,277.87
SP,santa rita d'oeste,3,3,178.57
SP,santa lucia,3,3,388.89
SP,santa cruz da conceicao,3,4,408.9
BA,belo campo,3,3,174.47
BA,barra do mendes,3,3,323.99
BA,barra do choca,3,3,799.0
SP,sabino,3,3,723.0
SP,riolandia,3,3,398.79999999999995
SP,ribeirao do sul,3,3,357.9
MT,rio branco,3,3,83.89
MT,dom aquino,3,3,449.79999999999995
SP,ribeira,3,3,209.28
BA,cacule,3,3,529.78
BA,buerarema,3,3,1051.8
SP,reginopolis,3,3,1552.99
SP,quadra,3,3,443.9
BA,candido sales,3,3,396.78999999999996
BA,caravelas,3,3,356.4
SP,poloni,3,3,163.12
BA,crisopolis,3,3,185.70000000000002
BA,coronel joao sa,3,3,587.99
BA,conceicao do jacuipe,3,3,177.89
BA,dom basilio,3,3,100.28
BA,curaca,3,3,308.9
MT,vila rica,3,3,221.82
MT,vera,3,3,262.79
MT,terra nova do norte,3,3,408.8
MT,castanheira,3,3,128.98000000000002
MT,barra do bugres,3,4,840.25
BA,ibicoara,3,3,299.2
BA,formosa do rio preto,3,3,1398.13
SP,ouro verde,3,3,307.96999999999997
SP,oscar bressane,3,3,301.8
SP,oriente,3,3,1017.2700000000001
SP,nuporanga,3,3,821.8
SP,neves paulista,3,3,112.58
BA,itajuipe,3,3,734.49
SP,mombuca,3,3,107.13999999999999
SP,mineiros do tiete,3,3,216.15
BA,ituacu,3,3,398.5
BA,itirucu,3,3,653.28
BA,itatim,3,3,312.69
BA,itarantim,3,3,478.97
BA,itapitanga,3,3,205.70000000000002
PA,breu branco,3,3,481.74
PA,brasil novo,3,3,304.9
MT,alto taquari,3,3,750.88
MT,alto boa vista,3,5,418.0
PA,augusto correa,3,3,347.99
BA,itambe,3,3,368.6
BA,itamari,3,3,268.98
SP,manduri,3,3,239.62
BA,jacaraci,3,4,911.79
BA,itubera,3,3,100.73
SP,lupercio,3,3,133.79
SP,luiziania,3,3,225.49
PA,itaituba,3,3,243.88
PA,hidreletrica tucurui,3,3,564.78
PA,goianesia do para,3,3,861.99
PA,garrafao do norte,3,3,662.89
PA,concordia do para,3,3,929.78
PA,capitao poco,3,3,405.38
PA,capanema,3,3,475.98
SP,lagoinha,3,3,605.98
SP,joao ramalho,3,3,407.89
BA,nazare,3,3,419.84000000000003
SP,jaborandi,3,3,126.29
BA,pindobacu,3,3,169.9
BA,nova soure,3,3,255.52
BA,presidente dutra,3,3,194.8
SP,inubia paulista,3,3,304.98
MS,nova alvorada do sul,3,3,380.85
MS,mundo novo,3,3,667.99
SP,indiapora,3,3,356.67
SP,indiana,3,3,343.89
BA,rodelas,3,3,404.9
BA,rio real,3,3,386.0
BA,rio do pires,3,4,552.8
BA,rio de contas,3,3,226.70000000000002
BA,quixabeira,3,3,216.94
SP,ilha comprida,3,3,212.98000000000002
BA,sao domingos,3,3,165.31
BA,santana,3,3,197.3
BA,santaluz,3,3,274.89
BA,santa ines,3,3,293.9
SP,herculandia,3,3,184.89000000000001
BA,sao francisco do conde,3,3,276.8
SP,guapiara,3,3,210.29000000000002
MS,dois irmaos do buriti,3,3,826.9
SP,gastao vidigal,3,3,216.88
BA,uaua,3,3,393.98
BA,teofilandia,3,3,183.88
BA,tanque novo,3,3,329.59
BA,tabocas do brejo velho,3,3,139.88
SP,estrela do norte,3,3,173.79
BA,utinga,3,3,323.89
CE,alto santo,3,3,622.89
BA,xique-xique,3,3,179.79000000000002
SP,dumont,3,3,289.70000000000005
SP,cruzalia,3,3,292.4
CE,boa viagem,3,3,450.99
CE,beberibe,3,3,1736.7
CE,baturite,3,3,447.97
CE,aurora,3,3,367.69
CE,aracoiaba,3,3,497.79999999999995
MS,jardim,3,3,256.0
MS,ivinhema,3,3,243.69
MS,itapora,3,3,197.88
CE,catarina,3,3,204.98
CE,carius,3,3,477.88
CE,carire,3,3,144.79
SP,capela do alto,3,3,833.99
CE,ipueiras,3,3,1547.29
CE,ibiapina,3,3,197.89
CE,itaitinga,3,3,558.9
CE,monsenhor tabosa,3,3,329.8
CE,marco,3,3,582.6
CE,maranguape,3,3,289.87
CE,parambu,3,4,141.86
CE,novo oriente,3,3,231.98000000000002
CE,nova olinda,3,3,1490.8
SP,barra do turvo,3,3,293.9
PA,tucuma,3,3,404.25
CE,reriutaba,3,3,1093.32
CE,redencao,3,4,1104.68
CE,pereiro,3,3,285.89
SP,areiopolis,3,3,896.49
SP,areias,3,3,441.86
SP,arealva,3,3,176.69
SP,arandu,3,3,235.60000000000002
CE,sucesso,3,3,352.9
CE,santana do cariri,3,3,839.8
DF,taguatinga,3,4,429.1
CE,ubajara,3,3,1178.9
SP,alambari,3,3,179.88
PB,coremas,3,3,284.69000000000005
MS,bela vista,3,3,466.38
SP,aguas de santa barbara,3,3,154.9
SE,umbauba,3,3,178.9
SE,sao francisco,3,3,934.9
SE,propria,3,3,382.89
SE,cedro de sao joao,3,3,1999.99
ES,conceicao da barra,3,3,306.87
SE,barra dos coqueiros,3,3,484.82000000000005
SC,witmarsum,3,3,147.79
ES,itarana,3,3,789.37
SC,urubici,3,3,305.69
SC,timbe do sul,3,3,212.79000000000002
SC,sao ludgero,3,3,673.3199999999999
SC,sao jose do cerrito,3,3,278.89
SC,sangao,3,3,264.78999999999996
GO,aragarcas,3,3,156.88
PB,imaculada,3,3,340.89
PB,cuite,3,3,678.89
GO,americano do brasil,3,3,291.49
SC,riqueza,3,3,248.9
SC,rio fortuna,3,3,469.39
SC,rio do oeste,3,3,364.89
SC,pouso redondo,3,3,597.29
SC,ponte serrada,3,3,423.9
SC,petrolandia,3,5,589.85
SC,palmeira,3,3,626.9
SC,nova veneza,3,3,422.89
SC,nova erechim,3,3,254.79
SC,meleiro,3,3,210.8
SC,massaranduba,3,3,347.86
SC,major vieira,3,3,256.89
SC,lontras,3,3,402.5
PB,mari,3,3,264.55
GO,indiara,3,4,369.91
GO,inaciolandia,3,3,842.99
GO,iaciara,3,3,666.99
SC,ita,3,3,317.89
SC,irani,3,4,294.39
GO,jussara,3,3,82.78999999999999
GO,itapaci,3,3,237.8
GO,itaja,3,3,902.0
SC,grao para,3,3,220.8
SC,governador celso ramos,3,3,389.97
SC,dionisio cerqueira,3,3,428.0
GO,paranaiguara,3,3,236.89
GO,palmeiras de goias,3,3,334.8
SC,caibi,3,3,132.05
GO,sanclerlandia,3,4,419.79
GO,piranhas,3,4,718.79
GO,serranopolis,3,3,1002.88
GO,sao simao,3,3,238.70000000000002
PB,pocinhos,3,3,223.8
MS,aquidauana,3,3,100.8
GO,sao joao d'alianca,3,3,743.53
GO,santa fe de goias,3,4,1737.6899999999998
SC,balneario rincao,3,3,393.0
SC,balneario gaivota,3,3,282.3
GO,vianopolis,3,3,529.6700000000001
GO,urutai,3,3,133.48000000000002
GO,uruana,3,3,1142.29
SC,anchieta,3,3,302.70000000000005
RS,vila langaro,3,3,140.64
RS,vila flores,3,3,289.89
RS,vera cruz,3,4,579.98
RS,vale real,3,3,210.53
PB,sume,3,3,248.89
PB,soledade,3,3,258.9
PB,sao bento,3,3,579.89
RS,tupandi,3,3,285.99
RS,tupancireta,3,4,378.77000000000004
RS,tucunduva,3,3,374.99
RS,trindade do sul,3,4,3266.99
RS,tres arroios,3,3,170.27
RS,toropi,3,3,1529.9
RS,tenente portela,3,3,482.79
RS,sobradinho,3,3,323.9
RS,sertao,3,3,309.49
MA,chapadinha,3,3,113.88
MA,cedral,3,3,1164.9
MG,virgem da lapa,3,3,737.9
MG,verissimo,3,3,294.12
RS,sao valentim,3,3,557.89
MA,fortuna,3,3,523.89
MA,estreito,3,3,305.89
MA,esperantinopolis,3,3,640.61
MA,dom pedro,3,3,333.77
MA,cururupu,3,3,629.26
MA,colinas,3,3,1128.87
MA,mirinzal,3,3,154.87
RS,restinga seca,3,3,254.69
MA,pindare mirim,3,3,481.9
MA,pedreiras,3,3,1002.69
MA,paraibano,3,3,259.90999999999997
RS,planalto,3,3,292.99
RS,pedro osorio,3,3,692.4499999999999
PE,camutanga,3,3,295.8
RS,parai,3,3,233.4
RS,pantano grande,3,3,297.79
MA,sao bernardo,3,3,706.79
MA,santa helena,3,3,649.7
RS,nova hartz,3,3,618.88
RS,nova alvorada,3,3,261.8
RS,morro reuter,3,3,627.34
RS,maximiliano de almeida,3,3,363.49
RS,manoel viana,3,3,208.79
RS,lavras do sul,3,3,593.8
RS,jaguari,3,3,157.89
RS,imigrante,3,3,305.9
MA,sao mateus do maranhao,3,3,710.2
RS,ilopolis,3,3,181.8
MG,aguas vermelhas,3,3,574.58
MG,abadia dos dourados,3,3,358.9
MG,tiros,3,3,175.89
MG,uniao de minas,3,3,87.09
MG,ubaporanga,3,3,288.78000000000003
MA,vitorino freire,3,3,1588.0
RS,gaurama,3,3,277.88
RS,entre-ijuis,3,3,454.5
MG,andrelandia,3,3,119.36
MG,alto jequitiba,3,3,211.89
MG,alterosa,3,3,252.3
MG,alfredo vasconcelos,3,3,567.99
RS,cruzeiro do sul,3,3,2235.9
RS,cristal,3,3,533.0
MG,antonio prado de minas,3,3,282.0
RS,colorado,3,3,202.70000000000002
MG,belo vale,3,3,313.8
MG,bandeira,3,3,347.71
MG,azurita,3,3,169.70000000000002
PE,jaqueira,3,3,578.99
PE,itapissuma,3,3,290.8
PE,itambe,3,3,259.88
PE,ipubi,3,3,400.47
PE,ibimirim,3,3,294.79
PE,iati,3,3,628.99
RS,capao do cipo,3,3,260.0
RS,campos borges,3,3,825.89
RS,cacequi,3,3,286.99
RS,barros cassal,3,3,729.0
MG,caiana,3,3,235.9
MG,cachoeira de pajeu,3,3,428.8
MG,cabo verde,3,3,458.78999999999996
RS,arvorezinha,3,4,262.5
RS,arroio grande,3,3,336.77
PE,lagoa grande,3,4,1018.36
PE,lagoa dos gatos,3,3,969.99
PE,joao alfredo,3,3,215.49
RO,urupa,3,3,253.57
MG,campestre,3,3,321.70000000000005
RO,sao miguel do guapore,3,4,399.44
RO,machadinho d'oeste,3,3,396.98
RO,guajara-mirim,3,3,118.89
MG,carbonita,3,4,755.87
RO,colorado do oeste,3,3,199.88
RO,alta floresta d'oeste,3,3,669.89
RN,upanema,3,3,1343.6
RN,sao miguel,3,4,846.86
RN,sao jose de mipibu,3,3,821.69
RN,patu,3,3,144.49
PE,oroco,3,3,294.9
PE,mirandiba,3,3,221.89
MG,setubinha,3,3,265.89
MG,carvalhopolis,3,3,240.32999999999998
MG,carrancas,3,3,134.79
MG,carneirinho,3,3,294.5
MG,carmo de minas,3,3,643.96
RN,jardim do serido,3,3,445.9
RN,goianinha,3,3,325.3
RN,caraubas,3,3,1059.29
RN,areia branca,3,3,183.6
MG,coluna,3,3,297.88
RN,apodi,3,3,377.89
MG,conceicao do para,3,3,694.99
MG,conceicao das alagoas,3,3,1542.4
RJ,sao jose do turvo,3,3,240.70000000000002
RJ,sao jose de uba,3,3,478.89
MG,sao tomas de aquino,3,3,309.8
PE,sanharo,3,3,1748.0
PE,saloa,3,3,1231.0
PE,pedra,3,3,267.68
MG,cristalia,3,3,418.7
MG,cristais,3,3,208.7
MG,coracao de jesus,3,3,123.9
RJ,rio claro,3,3,380.98
MG,descoberto,3,3,206.98000000000002
MG,delfinopolis,3,3,233.58999999999997
MG,gameleiras,3,3,423.89
MG,francisco sa,3,3,532.8
MG,francisco badaro,3,3,367.46
MG,florestal,3,3,299.5
RJ,ipiabas,3,4,568.87
MG,grao mogol,3,3,899.8
MG,goncalves,3,3,356.9
MG,iguatama,3,3,299.0
MG,ibiraci,3,3,388.8
MG,ibiai,3,3,556.89
MG,itacarambi,3,3,339.79
MG,ipiacu,3,3,429.88
RJ,arrozal,3,3,833.89
RJ,anta,3,3,241.88
PR,vere,3,3,598.39
PR,vera cruz do oeste,3,3,431.56
PR,ventania,3,3,166.76999999999998
PR,urai,3,3,283.9
PR,tomazina,3,3,348.8
PR,terra roxa,3,3,561.0699999999999
MG,itinga,3,3,363.5
MG,sao sebastiao do maranhao,3,3,206.79
MG,sao pedro dos ferros,3,4,763.79
MG,sao pedro da uniao,3,3,286.89
PR,sao pedro do ivai,3,3,424.74
PR,santo antonio do sudoeste,3,3,208.95
PR,santa terezinha de itaipu,3,3,328.94
PR,santa tereza do oeste,3,3,364.9
PR,santa isabel do ivai,3,3,425.9
MG,liberdade,3,3,107.22999999999999
MG,lajinha,3,3,515.0699999999999
PR,salgado filho,3,3,155.7
PR,reserva,3,3,308.6
PR,quinta do sol,3,3,118.99000000000001
MG,maria da fe,3,3,305.55
MG,manga,3,3,378.8
MG,madre de deus de minas,3,3,362.96000000000004
MG,luminarias,3,3,423.8
PR,pitanga,3,3,532.7
PI,barras,3,3,210.88
PE,tuparetama,3,3,309.8
MG,matipo,3,4,491.19000000000005
MG,mario campos,3,3,618.64
PR,paranacity,3,3,178.15
MG,montalvania,3,3,352.2
MG,morada nova de minas,3,3,658.89
MG,monte verde,3,3,343.09999999999997
PR,nova aurora,3,3,575.89
PR,morretes,3,3,587.98
PR,moreira sales,3,3,345.67
PR,maripa,3,3,361.97
MG,papagaios,3,4,269.67
PR,lobato,3,3,498.53999999999996
MG,pedrinopolis,3,3,481.01
MG,pedralva,3,3,743.97
MG,sao goncalo do para,3,3,734.9
PI,eliseu martins,3,3,318.98
PI,bom jesus,3,3,807.8
PR,jundiai do sul,3,3,337.96999999999997
PR,joaquim tavora,3,3,317.98
PR,japira,3,3,363.79
PR,janiopolis,3,3,265.97
PR,ivate,3,3,273.98
MG,piedade dos gerais,3,3,392.88
MG,piedade do rio grande,3,3,362.78
MG,pocrane,3,3,172.99
MG,piumhi,3,3,195.73000000000002
PR,florestopolis,3,3,492.70000000000005
MG,prados,3,3,204.79
MG,pouso alto,3,3,251.0
MG,pote,3,3,506.9
PI,fronteiras,3,3,1308.8000000000002
MG,sao joao do manteninha,3,3,474.89
MG,sao joao batista do gloria,3,3,359.6
MG,sao goncalo do rio preto,3,3,328.19
PR,entre rios do oeste,3,3,93.89
PR,cruz machado,3,3,441.77
PR,corbelia,3,3,733.8
PR,colonia castrolanda,3,3,824.03
PR,clevelandia,3,3,138.5
MG,resende costa,3,3,224.79000000000002
MG,recreio,3,3,264.98
PR,cerro azul,3,4,182.18
PR,carambei,3,3,390.8
MG,rubim,3,3,213.89
MG,ritapolis,3,3,145.69
MG,santa rita de minas,3,3,367.67
PI,paulistana,3,3,862.6700000000001
PI,luzilandia,3,3,161.8
PI,jose de freitas,3,3,257.9
PR,bela vista do paraiso,3,3,515.49
PR,areia branca dos assis,3,3,462.54
MG,santo antonio do itambe,3,3,225.06
MG,santana do manhuacu,3,3,228.89000000000001
PR,angulo,3,3,294.7
PR,altonia,3,3,494.9
PR,abatia,3,3,167.89
TO,formoso do araguaia,3,4,251.28000000000003
AL,coruripe,3,3,1222.3
TO,pedro afonso,3,3,235.89000000000001
AL,batalha,3,3,214.79000000000002
AC,cruzeiro do sul,3,3,957.79
MT,juscimeira,2,2,123.80000000000001
TO,pindorama do tocantins,2,2,99.66
TO,bandeirantes do tocantins,2,2,369.98
TO,arraias,2,2,197.9
TO,goianorte,2,2,184.99
AL,jequia da praia,2,2,251.91
AL,inhapi,2,2,979.9
AL,igreja nova,2,2,208.0
AL,igaci,2,2,319.89
AL,ibateguara,2,2,75.9
TO,alianca do tocantins,2,2,162.79
SP,zacarias,2,2,198.8
SP,vargem,2,2,78.8
AL,olho d'agua das flores,2,3,254.48
AL,mata grande,2,2,378.65000000000003
AL,maravilha,2,2,214.8
AL,junqueiro,2,2,360.89
SP,terra roxa,2,2,165.9
SP,tejupa,2,3,335.18
AL,sao jose da laje,2,2,219.9
MG,sao francisco de paula,2,2,78.89
MG,sao bras do suacui,2,2,95.99000000000001
PI,sao miguel do tapuio,2,2,465.0
AL,porto calvo,2,2,323.39
AL,pindoba,2,2,432.0
AL,paulo jacinto,2,2,368.89
SP,tapirai,2,2,108.65
SP,taciba,2,2,348.98
SP,sarapui,2,2,248.88
AP,laranjal do jari,2,2,318.8
AM,urucurituba,2,2,169.8
AL,satuba,2,2,333.73
AL,sao miguel dos campos,2,2,813.36
AL,sao luis do quitunde,2,2,239.3
SP,sao pedro do turvo,2,2,88.9
SP,sao jose do barreiro,2,3,207.59
MG,santana dos montes,2,2,241.0
PR,amapora,2,2,129.9
PR,alto parana,2,2,389.9
PR,alto alegre,2,2,167.99
PR,altamira do parana,2,2,259.1
MT,cotriguacu,2,2,167.66
MT,porto esperidiao,2,2,234.8
MT,paranatinga,2,2,2463.29
MT,nova olimpia,2,2,168.0
BA,abare,2,2,185.19
BA,abaira,2,2,157.99
SP,sao francisco,2,2,120.87
SP,santo antonio do pinhal,2,2,1128.9
BA,arembepe,2,2,429.7
PR,campina da lagoa,2,2,519.7
PR,cambira,2,2,432.0
PR,california,2,2,103.8
PR,cafeara,2,2,233.0
PR,borrazopolis,2,2,259.59000000000003
PR,bocaiuva do sul,2,2,49.89
PR,barbosa ferraz,2,3,497.9
MG,santo antonio do grama,2,2,239.9
BA,antonio cardoso,2,2,369.89
SP,santa mercedes,2,2,226.99
SP,santa maria da serra,2,2,143.64000000000001
SP,santa ernestina,2,2,208.16
BA,barro alto,2,2,91.99
BA,barra,2,2,143.9
BA,baianopolis,2,2,416.3
SP,salmourao,2,2,59.879999999999995
SP,rubiacea,2,2,218.8
SP,rinopolis,2,2,104.89
SP,rifaina,2,2,552.8
PI,piracuruca,2,2,235.9
PI,pimenteiras,2,2,102.5
PI,novo oriente do piaui,2,2,152.01
MG,santa cruz do prata,2,2,128.9
MG,santa cruz de salinas,2,2,220.9
MT,salto do ceu,2,2,140.39000000000001
MT,ribeiraozinho,2,2,299.98
MT,reserva do cabacal,2,2,383.9
MT,poxoreu,2,2,128.57
MT,gaucha do norte,2,2,136.48000000000002
MT,figueiropolis d'oeste,2,2,77.98
MT,denise,2,2,507.0
SP,ribeirao branco,2,2,452.99
PR,cantagalo,2,2,114.99
MG,salto da divisa,2,2,116.98
MG,romaria,2,2,264.9
MG,rodeiro,2,3,409.4
MG,santa rita do ibitipoca,2,2,184.7
MG,santa maria do suacui,2,2,454.9
MG,santa margarida,2,2,362.9
MG,santa helena de minas,2,2,248.33999999999997
BA,buritirama,2,2,251.9
BA,bonito,2,2,378.8
BA,boninal,2,2,717.6999999999999
BA,bom jesus da serra,2,2,279.89
SP,rechan,2,2,288.8
SP,queluz,2,2,213.74
BA,caldeirao grande,2,2,224.9
SP,presidente alves,2,2,112.61
SP,potim,2,2,249.8
SP,porangaba,2,2,166.39
SP,pontalinda,2,2,60.8
BA,catu de abrantes,2,2,1135.99
PR,congonhinhas,2,2,285.70000000000005
PR,colonia jordaozinho,2,2,843.4
MG,ribeirao vermelho,2,2,275.70000000000005
MG,riacho dos machados,2,3,284.0
MG,riachinho,2,2,82.34
BA,castro alves,2,2,58.9
BA,carinhanha,2,2,348.9
BA,cristopolis,2,2,63.41
BA,correntina,2,2,130.99
BA,conde,2,2,819.0
BA,conceicao da feira,2,2,603.99
SP,pindorama,2,2,368.9
SP,pedregulho,2,2,1039.4
SP,pedra bela,2,2,250.9
BA,fatima,2,2,451.9
BA,elisio medrado,2,2,79.82
BA,dario meira,2,2,138.99
MG,sao joao do oriente,2,2,279.9
MG,sao joao do manhuacu,2,2,154.8
MG,sao joao das missoes,2,2,119.99
MG,sao joao da mata,2,2,174.78
PR,espigao alto do iguacu,2,2,158.9
MT,tabapora,2,2,214.9
MT,carlinda,2,2,204.9
MT,campinapolis,2,3,324.86
MT,sao jose dos quatro marcos,2,2,226.99
MT,sao jose do rio claro,2,2,298.0
SP,pauliceia,2,2,421.27
SP,patrocinio paulista,2,2,1059.2
MG,pirauba,2,3,247.77
PR,florai,2,2,387.39
PR,flor da serra do sul,2,2,197.10000000000002
MG,presidente kubitschek,2,2,115.42999999999999
MG,porto firme,2,2,153.60999999999999
MG,ponto dos volantes,2,2,41.4
SP,paranapua,2,2,64.99000000000001
BA,ibipitanga,2,2,349.98
BA,ibiassuce,2,2,164.5
BA,guaratinga,2,2,42.99
BA,iguai,2,2,535.99
BA,ichu,2,2,160.98000000000002
BA,ibirataia,2,2,52.8
SP,nova canaa paulista,2,2,109.89000000000001
SP,nova campina,2,2,156.5
PR,inaja,2,2,56.9
PR,imbau,2,2,124.2
PR,guaraci,2,2,651.9
PR,grandes rios,2,2,128.99
MG,planura,2,2,102.16
SP,nossa senhora do remedio,2,2,131.9
SP,nipoa,2,2,337.8
SP,narandiba,2,2,408.97999999999996
SP,murutinga do sul,2,2,809.0
SP,motuca,2,2,158.9
BA,itagiba,2,2,126.89000000000001
BA,itagi,2,2,111.89000000000001
BA,itabatan,2,2,154.98000000000002
BA,irara,2,2,171.89000000000001
BA,iramaia,2,2,154.9
MG,pimenta,2,2,233.99
MG,piau,2,2,125.88999999999999
MG,perpetuo socorro,2,2,149.89000000000001
MG,periquito,2,2,1526.0
PR,itambaraca,2,2,269.8
PR,itaguaje,2,2,138.8
PR,ipora,2,2,194.89000000000001
PR,ipiranga,2,3,110.89
SP,moncoes,2,2,346.98
SP,mogi-mirim,2,2,89.8
SP,mirante do paranapanema,2,3,199.70000000000002
BA,itororo,2,2,619.2
BA,itapicuru,2,2,137.32999999999998
PA,bonito,2,2,304.9
PA,bom jesus do tocantins,2,3,407.9
PA,benevides,2,2,228.89000000000001
MT,arenapolis,2,2,328.85
MG,sao goncalo do abaete,2,2,177.99
PI,castelo do piaui,2,2,422.6
PI,buriti dos lopes,2,2,268.9
PR,jardim alegre,2,2,118.38000000000001
PR,jaboti,2,2,160.7
PR,ivai,2,2,610.7700000000001
MT,alto garcas,2,2,258.8
MS,sonora,2,2,57.98
SP,marinopolis,2,2,158.88
SP,mariapolis,2,2,111.9
SP,magda,2,2,458.99
BA,jussari,2,2,139.99
BA,jucurucu,2,2,409.98
BA,jaguaquara,2,2,192.4
SP,lucianopolis,2,2,142.9
SP,lourdes,2,2,193.7
BA,mascote,2,2,122.4
BA,maragogipe,2,2,152.8
BA,mairi,2,2,913.0
PR,lunardelli,2,2,214.89
PR,luiziana,2,2,149.85
PR,lindoeste,2,2,164.3
PR,kalore,2,2,429.99
MG,patrocinio do muriae,2,2,94.8
PR,juranda,2,2,40.9
PA,ipixuna do para,2,2,188.0
PA,curuca,2,3,524.7
SP,jumirim,2,3,337.6
SP,julio mesquita,2,2,909.99
BA,nova canaa,2,2,156.9
BA,muquem do sao francisco,2,2,61.32
BA,morpara,2,2,357.12
BA,milagres,2,2,502.53999999999996
SP,jaci,2,2,115.89
SP,itirapina,2,2,142.89999999999998
BA,pintadas,2,2,449.79999999999995
BA,pindai,2,2,134.8
BA,piata,2,2,80.97999999999999
PR,matelandia,2,2,57.980000000000004
PR,mariluz,2,2,308.99
MG,paiva,2,2,146.2
MG,pains,2,3,298.33
MG,ouro verde de minas,2,2,80.78999999999999
PR,lupionopolis,2,2,209.75
BA,paripiranga,2,2,77.71000000000001
BA,palmeiras,2,2,174.95
BA,oliveira dos brejinhos,2,2,138.9
BA,olindina,2,2,189.89000000000001
SP,itapirapua paulista,2,2,479.79999999999995
BA,pocoes,2,2,308.99
BA,piripa,2,2,71.99000000000001
SP,itaju,2,3,927.8
MG,montezuma,2,2,186.89000000000001
MG,monte formoso,2,2,72.99
PR,nova cantu,2,2,199.9
PR,nossa senhora das gracas,2,2,54.8
PR,mercedes,2,2,213.9
PR,maua da serra,2,2,129.99
MG,nazareno,2,2,161.8
SP,ipigua,2,2,247.24
PA,mojui dos campos,2,2,119.59
PA,mae do rio,2,2,148.89
BA,rio do antonio,2,2,259.0
BA,quijingue,2,2,228.08999999999997
BA,sao felipe,2,2,747.9
BA,santa teresinha,2,2,287.0
SP,iacri,2,2,56.98
PR,paraiso do norte,2,3,187.82
PR,palmeirinha,2,2,58.919999999999995
SP,guariroba,2,2,289.99
BA,serra dourada,2,2,197.14
BA,saude,2,2,119.4
BA,sapeacu,2,2,246.79000000000002
BA,sao jose da vitoria,2,2,175.65
SP,guaraci,2,2,479.79999999999995
SP,glicerio,2,2,333.99
SP,getulina,2,2,99.80000000000001
SP,gaviao peixoto,2,2,94.89
MS,deodapolis,2,2,76.8
PA,santa maria do para,2,2,106.99
PA,porto trombetas,2,2,241.8
PA,placas,2,2,220.29000000000002
PA,oeiras do para,2,2,178.64999999999998
PA,novo repartimento,2,2,155.0
MG,mato verde,2,3,420.43000000000006
MG,materlandia,2,2,79.98
MG,martinho campos,2,2,415.2
PR,perola d'oeste,2,2,619.9
PR,perola,2,2,272.74
PR,pato bragado,2,2,86.69999999999999
BA,tapiramuta,2,2,1298.99
BA,sitio do quinto,2,2,97.89
BA,serrolandia,2,2,325.0
SP,floreal,2,2,192.89000000000001
BA,vereda,2,2,309.4
PI,avelino lopes,2,2,72.89
PI,agua branca,2,2,132.9
PE,vicencia,2,2,268.0
PE,venturosa,2,2,1228.9
MG,medeiros,2,2,279.49
MG,matutina,2,2,134.89000000000001
BA,urucuca,2,2,195.9
BA,urandi,2,2,707.94
SP,espirito santo do turvo,2,2,229.70000000000002
SP,espigao,2,2,74.89
SP,echapora,2,2,787.47
CE,apuiares,2,2,339.89
CE,altaneira,2,2,369.6
CE,abaiara,2,2,262.9
BA,wanderley,2,2,288.98
SP,dobrada,2,2,437.5
CE,arneiroz,2,2,349.6
CE,aratuba,2,2,343.9
SP,corumbatai,2,2,49.59
PR,quitandinha,2,2,368.9
MG,machacalis,2,2,138.89
MG,luz,2,2,166.9
PR,porto amazonas,2,2,58.79
PA,sao sebastiao da boa vista,2,2,198.9
PA,sao joao de pirabas,2,2,228.89
PA,santana do araguaia,2,2,392.79999999999995
MS,jaraguari,2,2,75.0
MS,itaquirai,2,2,272.9
SP,coronel macedo,2,2,92.9
SP,coroados,2,2,209.9
CE,carnaubal,2,2,214.89000000000001
CE,caririacu,2,2,454.0
SP,canitar,2,2,287.25
SP,candido rodrigues,2,4,81.78999999999999
CE,frecheirinha,2,2,175.09
PR,santa izabel do oeste,2,2,319.89
MG,luizlandia do oeste,2,2,232.99
MG,luisburgo,2,2,246.98000000000002
MG,limeira do oeste,2,2,441.7
MG,leandro ferreira,2,2,208.9
PR,rondon,2,2,262.98
PR,roncador,2,2,158.98000000000002
CE,deputado irapuan pinheiro,2,2,169.98000000000002
SP,campina do monte alegre,2,2,237.9
SP,caiua,2,2,146.0
CE,iraucuba,2,2,189.89000000000001
CE,iracema,2,2,229.9
CE,ipaporanga,2,2,388.9
CE,jardim,2,2,392.65
PR,sao jorge do patrocinio,2,2,89.9
PR,sao joao do triunfo,2,2,163.82
PR,sao joao do ivai,2,2,193.9
PR,santa monica,2,2,332.88
SP,buritizal,2,2,66.99
CE,miraima,2,2,254.0
CE,milha,2,2,207.9
CE,milagres,2,2,334.0
CE,meruoca,2,2,95.0
CE,massape,2,2,155.9
CE,lavras da mangabeira,2,2,827.88
SP,bento de abreu,2,2,327.98
CE,pacoti,2,2,149.8
CE,oros,2,2,100.65
CE,ocara,2,2,109.88999999999999
PR,tamarana,2,2,103.9
PR,serranopolis do iguacu,2,2,274.89
PR,sapopema,2,2,154.98000000000002
PR,sao tome,2,2,234.07
MG,ladainha,2,2,171.14
MG,juvenilia,2,2,77.47999999999999
MG,jequitiba,2,2,636.9
MG,jequitai,2,2,204.18
PB,areia,2,2,119.80000000000001
PB,alhandra,2,2,1037.0
PB,alagoinha,2,2,269.9
PB,agua branca,2,2,204.99
PA,vigia,2,2,158.8
CE,quixere,2,2,744.3
CE,quixelo,2,2,115.99
CE,potengi,2,2,245.89000000000001
CE,pentecoste,2,2,239.8
CE,penaforte,2,2,479.89
CE,pedra branca,2,2,36.89
SP,arapei,2,2,324.89
SP,aparecida de sao manuel,2,2,226.3
CE,trairi,2,2,457.0
PE,tacaratu,2,2,204.89000000000001
PE,serrita,2,2,428.9
MG,sao roque de minas,2,2,169.89
MG,sao jose do goiabal,2,2,202.9
PE,sao jose do belmonte,2,2,228.9
PR,tapejara,2,2,355.9
CE,solonopole,2,2,729.89
CE,sao luis do curu,2,2,173.9
SP,alvaro de carvalho,2,2,358.0
SP,alvares florence,2,2,185.76
CE,varzea alegre,2,2,140.29
CE,uruoca,2,2,219.70000000000002
PR,vila nova,2,2,85.47
PR,turvo,2,2,112.1
PR,tunas do parana,2,2,198.9
MG,itatiaiucu,2,2,129.9
MG,itamogi,2,2,229.9
MG,jacinto,2,2,113.99
MG,itueta,2,2,448.89
PB,cubati,2,2,135.89000000000001
PB,conceicao,2,2,114.49
MS,bataypora,2,2,256.89
SP,aguas de sao pedro,2,2,274.99
SE,tomar do geru,2,2,228.79000000000002
SE,tobias barreto,2,2,209.99
ES,braco do rio,2,2,101.49
ES,alto rio novo,2,2,266.5
MG,irai de minas,2,2,414.89
MG,inimutaba,2,2,266.7
MG,inhauma,2,2,124.97999999999999
MG,inconfidentes,2,2,99.99000000000001
PR,wenceslau braz,2,2,188.0
SE,nossa senhora da gloria,2,2,221.45000000000002
SE,itabaianinha,2,2,157.8
ES,governador lindenberg,2,2,101.97
ES,celina,2,2,174.9
SE,carmopolis,2,2,87.31
SE,capela,2,3,580.9399999999999
SE,caninde de sao francisco,2,2,250.8
SC,zortea,2,2,99.80000000000001
SC,xavantina,2,2,176.02
ES,jeronimo monteiro,2,2,284.0
ES,jacigua,2,2,134.49
ES,iuna,2,2,131.0
ES,itaoca,2,2,404.9
ES,irupi,2,2,242.99
ES,muniz freire,2,2,238.9
MG,goiabeira,2,2,259.98
RJ,engenheiro passos,2,2,250.89000000000001
MG,imbe de minas,2,2,209.0
MG,icarai de minas,2,2,254.9
SC,sao pedro de alcantara,2,2,263.0
SC,sao martinho,2,2,451.0
SC,sao joao do sul,2,2,861.0
ES,presidente kennedy,2,2,238.64999999999998
ES,vila nelita,2,2,119.9
SC,sao domingos,2,2,148.99
SC,santa rosa de lima,2,3,180.15
GO,araguapaz,2,2,120.9
PE,santa maria da boa vista,2,2,412.08
MG,senhora de oliveira,2,2,116.9
MG,senador modestino goncalves,2,2,119.32
MG,senador firmino,2,2,138.57
MG,goiana,2,3,88.7
PB,junco do serido,2,2,239.89
PB,itaporanga,2,2,263.8
PB,frei martinho,2,2,268.9
GO,alvorada do norte,2,3,164.88
GO,alto horizonte,2,2,233.91
SC,rio das antas,2,2,176.8
SC,rancho queimado,2,2,312.89
SC,peritiba,2,2,106.9
SC,paulo lopes,2,2,238.99
SC,passos maia,2,2,208.9
GO,campo alegre de goias,2,2,175.89000000000001
GO,cachoeira dourada,2,2,148.9
MG,francisco dumont,2,2,108.89
MG,formoso,2,2,828.99
RJ,glicerio,2,2,405.99
MG,guidoval,2,2,364.9
MG,guarda-mor,2,2,83.9
MG,guarara,2,2,501.99
MG,guaraciaba,2,2,199.8
PE,sao jose da coroa grande,2,2,218.9
GO,brazabrantes,2,2,53.5
GO,bonfinopolis,2,2,441.87
SC,nova itaberaba,2,2,308.89
GO,corumba de goias,2,2,126.99
GO,cavalcante,2,2,158.99
GO,carmo do rio verde,2,2,169.89
SC,monte carlo,2,3,309.5
SC,mondai,2,2,409.0
SC,maracana,2,2,238.0
SC,luiz alves,2,2,114.0
SC,jaguaruna,2,2,162.9
SC,jabora,2,2,267.9
RJ,monnerat,2,2,284.84000000000003
MG,ferros,2,2,119.6
MG,estrela do indaia,2,2,112.80000000000001
MG,fruta de leite,2,2,178.9
MG,virgolandia,2,2,380.0
PB,picui,2,2,107.99
PB,pedras de fogo,2,2,159.99
GO,doverlandia,2,2,277.91999999999996
GO,domiciano ribeiro,2,2,114.89
GO,damianopolis,2,2,33.64
GO,cumari,2,2,199.9
GO,itaguacu,2,2,82.89
GO,hidrolina,2,2,181.47
SC,ipira,2,2,130.20000000000002
SC,ibicare,2,2,227.4
GO,jesupolis,2,2,159.33
MG,cruzeiro da fortaleza,2,2,114.9
RJ,passa tres,2,2,63.85
MG,durande,2,2,117.49000000000001
MG,dona euzebia,2,2,316.89
MG,dom vicoso,2,2,272.3
MG,divisa alegre,2,2,190.99
GO,itapirapua,2,2,459.79999999999995
GO,itaguaru,2,2,84.89
GO,nazario,2,2,237.89000000000001
GO,mundo novo,2,2,306.0
MG,coroaci,2,2,338.9
RJ,raposo,2,3,584.7
MG,dionisio,2,2,118.80000000000001
MG,diogo de vasconcelos,2,2,191.62
GO,matrincha,2,2,163.29
GO,mara rosa,2,2,143.9
GO,mambai,2,2,816.99
SC,celso ramos,2,2,1136.79
SC,campo alegre,2,2,178.9
GO,santa cruz de goias,2,2,709.0
GO,portelandia,2,2,93.99000000000001
GO,simolandia,2,2,138.99
PB,rio tinto,2,2,439.9
MS,anastacio,2,2,116.9
MS,agua clara,2,2,219.89000000000001
SC,botuvera,2,2,181.9
SC,bom jesus,2,2,819.89
SC,aurora,2,2,371.9
MG,sao thome das letras,2,2,52.8
PE,santa cruz,2,2,263.9
PE,rio formoso,2,2,215.6
PE,riacho das almas,2,2,203.9
PE,paudalho,2,2,878.9
MG,cristiano otoni,2,2,210.2
MG,crisolita,2,2,103.9
GO,vicentinopolis,2,2,384.79999999999995
GO,turvania,2,2,83.7
SC,armazem,2,2,249.9
SC,antonio carlos,2,2,215.8
SC,anitapolis,2,2,608.99
SC,alfredo wagner,2,2,794.8
SC,agronomica,2,2,204.87
RS,victor graeff,2,2,142.8
RJ,werneck,2,2,403.89
RJ,visconde de maua,2,3,140.59
RJ,tocos,2,2,338.9
RJ,santo eduardo,2,2,215.0
PB,sape,2,2,1959.99
RS,tuparendi,2,2,183.49
MA,bom jesus das selvas,2,2,175.9
MA,boa vista do gurupi,2,2,93.89
MA,bacuri,2,3,315.42
MA,arari,2,2,708.8
RS,sinimbu,2,2,81.78
MA,coelho neto,2,3,314.9
MA,carutapera,2,2,174.9
MA,carolina,2,2,429.79999999999995
MA,capinzal do norte,2,2,395.0
MG,chaveslandia,2,2,233.79000000000002
MG,chapada do norte,2,2,373.9
MG,chale,2,2,116.4
MG,chacara,2,2,175.7
RN,alexandria,2,2,159.8
RN,acu,2,2,455.59000000000003
MA,campestre do maranhao,2,2,249.89
PE,afranio,2,2,357.9
MG,varzelandia,2,2,98.89
MG,varjao de minas,2,2,105.8
RS,seberi,2,2,130.39000000000001
RS,sao vendelino,2,2,155.98000000000002
RS,sao paulo das missoes,2,2,404.87
RS,sao jose do hortencio,2,2,322.89
RS,sao francisco de assis,2,2,109.89
RS,santo antonio do palma,2,2,73.89
RS,santana da boa vista,2,2,79.89
RS,santa clara do sul,2,2,339.99
RS,santa barbara do sul,2,2,143.8
MA,matoes do norte,2,2,698.9
MA,mata roma,2,2,193.0
RN,guamare,2,2,156.8
RN,extremoz,2,2,111.78999999999999
RN,ceara-mirim,2,2,305.46000000000004
RN,carnaubais,2,2,339.0
MA,maioba,2,2,648.89
RS,rodeio bonito,2,2,212.8
RS,roca sales,2,2,177.9
RS,redentora,2,3,354.59000000000003
RS,quevedos,2,2,90.9
RS,putinga,2,2,144.8
MA,porto franco,2,2,279.99
RN,lagoa nova,2,2,113.80000000000001
MG,carlos chagas,2,2,124.80000000000001
MG,careacu,2,2,116.13
RN,joao camara,2,2,1379.8000000000002
RN,itau,2,2,666.8
RN,ielmo marinho,2,2,148.70000000000002
MA,pastos bons,2,2,137.9
MA,olho d'agua das cunhas,2,2,312.99
RS,protasio alves,2,2,122.9
PE,caraiba,2,2,416.89
PE,canhotinho,2,2,367.0
PE,camocim de sao felix,2,2,362.9
PE,buenos aires,2,2,247.9
PE,bodoco,2,2,202.8
PE,belem do sao francisco,2,2,654.5
PE,barra de guabiraba,2,2,486.4
PE,aracoiaba,2,2,78.67
PE,amaraji,2,2,476.89
RN,martins,2,2,177.89000000000001
PE,panelas,2,2,161.79000000000002
PE,moreilandia,2,2,230.9
MG,silvianopolis,2,3,132.5
MG,serro,2,2,837.89
MA,sao domingos do maranhao,2,2,127.88999999999999
MA,sao bento,2,2,569.0
MA,santa luzia,2,2,242.7
RS,novo barreiro,2,2,197.59
RS,nova palma,2,2,428.9
RS,nova esperanca do sul,2,2,259.4
RS,nonoai,2,2,175.9
RS,montauri,2,2,429.89
RS,mato leitao,2,2,179.0
RS,macambara,2,2,162.74
RS,jari,2,4,354.8
RN,santana do serido,2,2,779.7
RN,rodolfo fernandes,2,2,99.89
RN,portalegre,2,2,408.8
RN,pendencias,2,2,326.5
RN,nova cruz,2,3,462.88
RS,irai,2,2,557.89
RS,ipe,2,2,173.9
MA,tutoia,2,2,449.89
MA,sucupira do norte,2,2,319.9
MA,satubinha,2,2,138.79
RS,ibiraiaras,2,2,232.98
RS,ibiaca,2,2,278.89
RS,guarani das missoes,2,2,68.66
MG,agua comprida,2,2,106.9
MG,acaiaca,2,2,164.9
RN,serra de sao bento,2,2,236.9
RN,sao vicente,2,2,264.89
RN,sao paulo do potengi,2,2,229.9
RN,sao miguel do gostoso,2,2,398.9
MG,taquaracu de minas,2,2,358.0
MG,tabuleiro,2,2,324.89
MG,turvolandia,2,2,143.9
RS,glorinha,2,2,249.8
RS,formigueiro,2,2,279.8
RS,fazenda vilanova,2,2,157.8
MG,alvarenga,2,2,211.0
MG,alto caparao,2,2,478.9
MG,alpercata,2,2,228.8
RS,dona francisca,2,2,258.7
RS,david canabarro,2,2,167.88
RS,crissiumal,2,2,1589.0
RS,coxilha,2,2,115.9
RS,coqueiro baixo,2,2,86.99
MG,araponga,2,2,239.9
MG,aracitaba,2,2,119.80000000000001
MG,capetinga,2,2,198.9
MG,cantagalo,2,2,232.95
RO,extrema,2,3,809.9
RO,costa marques,2,2,1534.9
RO,buritis,2,2,240.98
MG,antonio pereira,2,2,88.99000000000001
RS,cerro grande do sul,2,2,184.0
MG,bandeira do sul,2,2,414.9
MG,baldim,2,2,650.99
MG,ataleia,2,2,164.8
PE,itaquitinga,2,2,64.89
RS,acegua,2,2,209.9
RO,seringueiras,2,2,395.99
MG,campanario,2,2,278.7
RO,sao francisco do guapore,2,2,284.9
RO,presidente medici,2,2,119.89000000000001
RO,nova mamore,2,2,594.9
RO,nova brasilandia d'oeste,2,2,402.79999999999995
MG,caputira,2,2,454.28
PE,itapetim,2,2,280.8
PE,inaja,2,2,369.4
PE,gloria do goita,2,2,516.99
PE,dormentes,2,2,946.8
PE,cumaru,2,2,330.99
PE,cortes,2,2,249.89000000000001
RS,capela de santana,2,2,352.0
RS,capao da porteira,2,2,157.0
MG,bias fortes,2,2,80.9
MG,serrania,2,2,345.89
MG,serra azul de minas,2,2,344.99
MG,sericita,2,2,216.32
PE,macaparana,2,2,144.88
PE,lagoa do ouro,2,2,305.9
PE,lagoa do carro,2,2,746.77
PE,jupi,2,2,604.9
PE,jatoba,2,3,415.3
PE,jatauba,2,2,126.89000000000001
RS,agua santa,2,2,163.9
RS,campo novo,2,2,539.79
RS,campina das missoes,2,2,155.8
RS,campestre da serra,2,2,1348.99
MG,bras pires,2,2,76.8
MG,bonfinopolis de minas,2,2,1387.2
RS,boqueirao do leao,2,2,227.9
RS,bom retiro do sul,2,2,1379.0
RS,barracao,2,2,98.49
MG,cachoeira do campo,2,2,828.99
MG,cachoeira da prata,2,2,169.8
MG,cabeceira grande,2,3,265.89
RS,aurea,2,2,409.5
RS,augusto pestana,2,2,76.88
RS,arroio do tigre,2,2,285.0
RS,ararica,2,2,187.0
RS,ametista do sul,2,2,242.8
RS,ajuricaba,2,2,191.9
TO,miranorte,2,2,635.9
AL,boca da mata,2,2,219.73000000000002
TO,couto de magalhaes,2,2,194.89
TO,colmeia,2,2,105.0
TO,cariri do tocantins,2,2,270.89
TO,barrolandia,2,2,80.99
AL,feliz deserto,2,2,309.89
AL,colonia leopoldina,2,2,477.98
TO,parana,2,2,108.88
AL,belem,2,2,469.99
AL,barra de sao miguel,2,2,155.98000000000002
AL,barra de santo antonio,2,2,567.0
AL,anadia,2,2,379.89
AC,xapuri,2,2,288.93
AC,senador guiomard,2,2,409.98
TO,novo jardim,1,1,23.9
AC,brasileia,1,1,59.699999999999996
AC,epitaciolandia,1,1,92.34
AC,manoel urbano,1,1,194.99
AC,porto acre,1,1,74.9
AL,agua branca,1,1,63.8
AL,atalaia,1,1,89.58
AL,dois riachos,1,1,104.99
PI,sao lourenco do piaui,1,1,152.49
PI,sao jose do piaui,1,1,149.9
PI,sao jose do divino,1,1,579.0
PI,santa cruz do piaui,1,1,119.99
PI,rio grande do piaui,1,1,24.9
TO,fatima,1,1,59.9
TO,esperantina,1,1,84.44
TO,duere,1,1,115.9
TO,divinopolis do tocantins,1,1,120.99
AL,girau do ponciano,1,1,39.9
TO,aparecida do rio negro,1,1,115.0
TO,ananas,1,1,96.8
TO,almas,1,1,78.0
SP,venda branca,1,1,117.3
SP,ubirajara,1,1,79.9
SP,turmalina,1,1,28.0
MG,braunas,1,1,89.9
MG,brasopolis,1,1,99.99
MG,brasilandia de minas,1,1,76.25
MG,bonito de minas,1,1,99.99
RS,bossoroca,1,1,155.99
RS,boa vista do sul,1,1,27.99
RS,boa vista do cadeado,1,1,429.98
RS,boa vista do burica,1,1,229.99
RS,boa vista das missoes,1,1,349.9
RS,barra do rio azul,1,1,99.0
RS,barao do triunfo,1,1,79.99
RS,barao de cotegipe,1,2,126.88999999999999
RS,barao,1,1,31.9
MG,camacho,1,1,59.99
MG,cajuri,1,1,53.9
MG,cachoeira dourada,1,1,119.9
MG,bom jesus do amparo,1,1,199.89
MG,bom jesus da penha,1,2,85.89
MG,serranopolis de minas,1,1,119.9
MG,serra do salitre,1,1,49.99
MG,serra bonita,1,1,169.99
PE,jurema,1,1,29.5
RS,agudo,1,1,17.0
RS,aguas claras,1,1,95.8
MG,bertopolis,1,1,65.9
MG,berizal,1,1,189.9
MG,berilo,1,1,55.9
RS,candido godoi,1,1,900.0
RS,cambara do sul,1,1,372.0
RS,caibate,1,1,319.9
MG,bugre,1,1,187.9
MG,brejo bonito,1,1,139.9
MG,bela vista de minas,1,1,119.9
MG,barra longa,1,1,1300.0
RS,caseiros,1,1,109.9
RR,bonfim,1,1,89.9
MG,canaa,1,1,54.99
MG,campo florido,1,1,59.8
MG,campo azul,1,1,79.9
MG,campo alegre de minas,1,1,119.0
RO,mutum parana,1,1,39.9
RO,mirante da serra,1,1,120.9
RO,ministro andreazza,1,1,69.9
PE,flores,1,1,230.70000000000002
PE,ferreiros,1,1,95.0
PE,cupira,1,1,39.9
RS,capivari do sul,1,1,159.0
RS,capitao,1,1,107.8
MG,capim branco,1,2,152.78
MG,capela nova,1,1,89.77
MG,caparao,1,1,49.9
RO,cujubim,1,1,89.9
RO,cerejeiras,1,1,117.99
RO,castanheiras,1,1,42.9
RO,candeias do jamari,1,1,279.0
RO,cacaulandia,1,1,72.9
RO,cabixi,1,1,149.9
RS,constantina,1,1,330.0
RS,colinas,1,1,32.99
RS,ciriaco,1,1,229.0
RS,chiapetta,1,1,129.99
RS,charrua,1,1,125.0
RS,cerro grande,1,1,52.9
RS,cerrito,1,1,59.9
RS,estrela velha,1,1,14.9
RS,esmeralda,1,1,145.0
RS,erval grande,1,2,395.9
RS,erebango,1,1,119.99
MG,antonio carlos,1,1,29.9
MG,angustura,1,1,139.0
MG,andrequice,1,1,199.0
MG,amparo da serra,1,1,49.95
RS,dezesseis de novembro,1,1,79.9
RS,cotipora,1,1,112.0
RS,coqueiros do sul,1,1,25.73
MG,arapua,1,1,89.0
MG,arantina,1,1,180.0
MG,antunes,1,1,119.8
MG,capitao eneas,1,1,65.6
MG,capitao andrade,1,1,199.0
PE,cha de alegria,1,1,79.99
MG,tocos do moji,1,1,55.0
MG,taparuba,1,1,89.0
MG,urucania,1,1,149.0
MG,uruana de minas,1,1,17.9
MG,umburatiba,1,1,109.99
MG,ubai,1,1,43.5
MG,tuparece,1,1,13.5
RS,gramado xavier,1,1,52.9
RS,gramado dos loureiros,1,1,209.99
RS,general camara,1,1,89.0
RS,garruchos,1,1,62.9
RS,fortaleza dos valos,1,1,100.0
RS,fontoura xavier,1,1,199.0
RS,faxinalzinho,1,1,19.9
RS,eugenio de castro,1,1,97.0
MG,alagoa,1,1,77.68
MG,acucena,1,1,38.0
RO,alvorada d'oeste,1,1,359.98
RO,alto paraiso,1,1,1200.0
RN,vila flor,1,1,99.73
RN,vicosa,1,1,50.9
RN,vera cruz,1,1,39.99
RN,tibau do sul,1,1,99.99
RN,tenente ananias,1,1,229.9
RN,sitio novo,1,1,149.9
RN,severiano melo,1,1,120.0
RN,sao tome,1,1,27.99
RN,sao rafael,1,1,19.9
RN,sao jose do serido,1,1,149.9
PE,correntes,1,1,169.9
PE,cha grande,1,1,164.89
RS,itatiba do sul,1,1,39.9
RS,itaara,1,1,56.99
RS,ipiranga do sul,1,1,109.9
RS,ipiranga,1,1,79.0
MA,vitoria do mearim,1,1,14.0
MA,vargem grande,1,1,79.9
MA,sitio novo,1,1,24.99
MA,senador la rocque,1,1,90.0
MA,sao vicente ferrer,1,1,205.9
MA,sao pedro da agua branca,1,1,309.9
RS,ibarama,1,1,149.0
RS,hulha negra,1,1,329.0
RS,herveiras,1,1,109.0
RS,herval,1,1,169.9
RS,guabiju,1,1,33.6
MG,alexandrita,1,1,99.8
RS,lagoa dos tres cantos,1,1,74.9
RN,sao jose do campestre,1,1,289.0
RN,sao joao do sabugi,1,1,26.9
RN,santo antonio,1,1,471.8
RN,santa maria,1,1,19.83
RN,riacho da cruz,1,1,129.9
RN,poco de pedra,1,1,174.0
RN,pedro velho,1,1,61.99
RN,pedra preta,1,1,49.9
RN,monte alegre,1,1,19.99
RN,montanhas,1,1,325.0
RN,messias targino,1,1,59.9
RS,jaquirana,1,1,499.0
RS,jacutinga,1,1,49.39
RS,jacuizinho,1,1,59.54
RS,ivora,1,1,149.9
RS,nova araca,1,1,119.99
RS,morro redondo,1,1,209.9
RS,monte bonito,1,1,29.5
RS,monte belo do sul,1,1,79.98
RS,monte alverne,1,1,268.0
RS,miraguai,1,1,169.97
RS,minas do leao,1,1,256.0
RS,mata,1,1,399.85
RS,marques de souza,1,1,29.9
RS,mariano moro,1,1,125.0
RS,maquine,1,1,122.99
RS,mampituba,1,1,40.95
RS,machadinho,1,1,48.0
RS,lindolfo collor,1,1,110.9
RS,liberato salzano,1,1,12.99
RS,lagoao,1,1,156.45
RS,osvaldo kroeff,1,1,239.99
MA,sao joao do paraiso,1,1,80.04
MA,sao joao batista,1,1,113.0
MA,sao francisco do brejao,1,1,31.9
MA,sao benedito do rio preto,1,1,95.0
MA,santa rita,1,1,89.9
MA,santa quiteria do maranhao,1,1,49.9
MA,santa luzia do parua,1,1,79.9
MA,sambaiba,1,1,178.9
MA,rosario,1,1,28.12
MA,presidente medici,1,1,105.0
RS,novo machado,1,1,59.99
RS,novo cabrais,1,1,55.0
RS,nova roma do sul,1,1,1106.99
RS,nova padua,1,1,69.9
RS,nova boa vista,1,1,52.9
PE,bom jardim,1,1,287.7
PE,passira,1,1,374.98
PE,orobo,1,1,99.9
PE,nossa senhora do o,1,1,37.0
PE,nazare da mata,1,1,99.99
PE,machados,1,1,89.9
MG,sobralia,1,1,24.9
MG,simao pereira,1,1,149.0
MG,silveira carvalho,1,1,28.9
MG,silvano,1,1,99.99
RN,marcelino vieira,1,1,117.7
RN,lagoa salgada,1,1,30.24
RS,pedras altas,1,1,89.9
RS,pareci novo,1,1,22.0
RS,paraiso do sul,1,1,28.99
RS,padre gonzales,1,1,50.0
MA,passagem franca,1,1,37.98
MA,parnarama,1,1,166.99
RS,progresso,1,1,215.0
RS,presidente lucena,1,1,16.99
RS,pouso novo,1,1,54.9
RS,porto lucena,1,1,59.89
RS,pontao,1,1,44.9
RS,polo petroquimico de triunfo,1,1,5.6
RS,piratini,1,1,69.9
RS,pinhal da serra,1,1,19.9
RS,picada cafe,1,1,32.0
MG,tumiritinga,1,1,459.0
PE,capoeiras,1,1,143.0
PE,calcado,1,1,199.0
PE,caetes,1,1,122.9
PE,buique,1,1,235.0
RS,rio dos indios,1,1,79.9
RS,rainha do mar,1,1,59.9
MA,presidente juscelino,1,1,249.99
RN,lagoa de velhos,1,1,199.0
MG,cascalho rico,1,1,69.0
MG,carmesia,1,1,241.1
RN,lagoa d'anta,1,1,170.0
RN,jose da penha,1,1,159.99
RN,jardim de piranhas,1,1,23.9
RN,japi,1,1,229.9
RN,janduis,1,1,84.99
RN,jandaira,1,1,109.9
RN,ipueira,1,1,169.99
MA,pocao de pedras,1,1,179.0
MA,pio xii,1,1,479.99
MA,peri mirim,1,1,34.99
RN,frutuoso gomes,1,1,79.99
RN,francisco dantas,1,1,198.9
RN,florania,1,1,35.5
RN,felipe guerra,1,1,122.99
RN,coronel joao pessoa,1,1,89.9
RN,carnauba dos dantas,1,1,129.99
RN,caicara do norte,1,1,1099.0
RN,bodo,1,1,48.9
RN,barauna,1,1,229.99
MG,coimbra,1,1,38.9
MA,maranhaozinho,1,1,40.9
MA,magalhaes de almeida,1,1,270.9
MA,loreto,1,1,1599.99
MA,lago verde,1,1,98.0
MA,joselandia,1,1,73.35
MA,jatoba,1,1,149.99
RS,sao joao da urtiga,1,1,139.9
RS,santo expedito do sul,1,1,209.99
RS,santo antonio do planalto,1,1,189.0
MA,icatu,1,1,778.0
MA,humberto de campos,1,1,45.9
MA,guimaraes,1,1,199.99
MA,governador eugenio barros,1,1,346.32
MA,goncalves dias,1,1,65.0
MA,formosa da serra negra,1,1,99.0
RS,santa maria do herval,1,1,99.99
RS,salvador do sul,1,1,179.0
MA,moncao,1,1,85.99
MA,miranda do norte,1,1,120.0
MA,matoes,1,1,72.0
RN,governador dix-sept rosado,1,1,159.9
RN,galinhos,1,1,240.0
PE,agrestina,1,1,1989.0
MG,vila pereira,1,1,92.8
MG,vieiras,1,1,325.0
MG,vermelho novo,1,1,33.87
MG,vermelho,1,1,98.0
MG,vargem grande do rio pardo,1,1,270.0
MG,vargem alegre,1,1,74.99
MG,urucuia,1,1,149.99
MA,cajari,1,1,289.0
MA,cajapio,1,1,89.99
RS,sao pedro do sul,1,1,98.7
RS,sao pedro do butia,1,1,99.9
RS,sao nicolau,1,1,122.99
RS,sao martinho,1,1,305.99
RS,sao jose do inhacora,1,1,77.99
RS,sao jorge,1,1,63.99
MA,centro novo do maranhao,1,1,299.99
MA,cantanhede,1,1,689.0
MA,candido mendes,1,1,239.8
MG,cocais,1,1,259.0
MG,claro dos pocoes,1,1,99.99
MG,claraval,1,1,171.0
MG,centralina,1,1,29.99
MG,central de santa helena,1,1,139.9
MG,cedro do abaete,1,1,42.99
RN,antonio martins,1,1,45.0
RN,angicos,1,1,65.99
RN,almino afonso,1,1,299.9
RN,agua nova,1,1,42.0
PE,altinho,1,1,13.9
PE,alianca,1,1,64.99
PE,agua preta,1,1,129.99
MA,arame,1,1,29.99
MA,araguana,1,1,119.0
RS,tres forquilhas,1,1,82.8
RS,travesseiro,1,1,16.6
RS,tiradentes do sul,1,1,46.86
RS,tavares,1,1,176.99
RS,taquarucu do sul,1,1,70.0
RS,tapera,1,1,61.8
RS,silveira martins,1,1,119.8
RS,sete de setembro,1,1,54.9
RS,sertao santana,1,1,20.9
RS,serio,1,1,22.9
RS,senador salgado filho,1,1,83.8
RS,selbach,1,1,49.9
RS,segredo,1,1,29.939999999999998
MA,cidelandia,1,1,375.96
PB,teixeira,1,1,34.9
PB,solanea,1,1,440.0
PB,serra branca,1,1,84.9
PB,sao mamede,1,1,86.0
PB,sao jose dos cordeiros,1,1,180.0
PB,sao francisco,1,1,89.0
PB,sao bentinho,1,1,35.0
PB,santo andre,1,1,54.9
PB,santa cecilia,1,1,149.9
RS,uniao da serra,1,1,18.5
MA,buriti,1,1,151.79
MA,brejo,1,1,99.99
MA,bom jardim,1,1,25.9
MA,bequimao,1,1,349.9
MA,benedito leite,1,1,95.9
MA,bela vista do maranhao,1,1,49.0
RS,unistalda,1,1,37.9
PB,varzea,1,1,98.99
RN,acari,1,1,364.0
RJ,valao do barro,1,1,67.1
RJ,tres irmaos,1,1,139.8
RJ,sao sebastiao do paraiba,1,1,540.0
RJ,sao sebastiao de campos,1,1,23.8
MG,confins,1,1,389.0
MG,conceicao do formoso,1,1,195.99
MG,conceicao da ibitipoca,1,1,39.99
MG,comercinho,1,1,129.0
RJ,sao jose do ribeirao,1,1,97.9
RJ,sao joao do paraiso,1,1,166.99
RJ,santa rita da floresta,1,1,79.0
PB,uirauna,1,1,199.9
PB,triunfo,1,1,159.9
SC,atalanta,1,1,263.99
SC,arvoredo,1,1,34.3
SC,arroio trinta,1,1,169.9
SC,angelina,1,1,126.99
SC,aguas mornas,1,1,89.15
SC,aguas frias,1,1,290.0
SC,agua doce,1,1,289.98
SC,agrolandia,1,1,49.9
SC,abdon batista,1,1,125.4
RS,vitoria das missoes,1,1,33.8
RS,vista alegre,1,1,22.0
RS,vila nova do sul,1,1,84.99
RS,vicente dutra,1,1,12.99
RS,vespasiano correa,1,1,144.99
RS,vanini,1,1,89.0
RS,vale do sol,1,1,21.99
SC,belmonte,1,1,149.7
MG,sapucaia,1,1,77.9
MG,sao vitor,1,1,99.9
MG,sao sebastiao do rio verde,1,1,278.0
PE,quixada,1,1,134.9
PE,quipapa,1,1,230.0
PE,pombos,1,1,105.0
PE,pocao,1,1,299.99
MG,crucilandia,1,1,17.0
MG,corrego fundo,1,1,129.0
MA,amapa do maranhao,1,1,15.9
MA,alto alegre do pindare,1,1,199.0
MA,alto alegre do maranhao,1,1,88.9
MA,alcantara,1,1,424.8
GO,turvelandia,1,1,27.3
GO,trombas,1,1,16.97
GO,teresina de goias,1,1,79.0
GO,sao patricio,1,1,158.7
GO,sao luiz do norte,1,1,129.99
GO,sao joao da parauna,1,1,159.99
PB,riacho de santo antonio,1,1,129.9
PB,remigio,1,1,149.9
PB,puxinana,1,1,219.0
PB,princesa isabel,1,1,258.0
PB,prata,1,1,54.9
PB,pitimbu,1,1,388.9
PB,pitanga de estrada,1,1,120.0
MS,bandeirantes,1,1,89.9
MS,anhandui,1,1,69.0
MS,angelica,1,1,53.9
MS,anaurilandia,1,1,69.99
SC,bom retiro,1,1,70.0
SC,coronel martins,1,2,121.30000000000001
SC,coronel freitas,1,1,79.99
SC,chapadao do lageado,1,1,272.70000000000005
SC,cerro negro,1,1,118.0
GO,palminopolis,1,1,199.0
GO,ouvidor,1,1,345.0
GO,ouro verde de goias,1,1,82.9
GO,novo planalto,1,1,27.99
GO,nova roma,1,1,49.99
GO,nova crixas,1,1,153.4
GO,nova aurora,1,1,490.0
GO,nova america,1,1,51.0
SC,caxambu do sul,1,1,19.5
SC,calmon,1,1,49.9
GO,pontalina,1,2,405.0
GO,planaltina de goias,1,2,95.6
GO,morro agudo de goias,1,1,32.9
GO,montividiu do norte,1,1,17.99
GO,mimoso de goias,1,1,159.9
MG,corrego danta,1,1,25.4
MG,coronel pacheco,1,1,99.9
MG,coronel murta,1,1,219.8
RJ,santa maria,1,1,8.0
RJ,santa isabel do rio preto,1,1,739.9
RJ,sacra familia do tingua,1,1,119.8
RJ,purilandia,1,1,166.99
RJ,pureza,1,1,49.9
MG,divinesia,1,1,249.9
MG,desterro do melo,1,1,24.9
MG,desterro de entre rios,1,1,39.9
MG,desembargador otoni,1,1,169.99
SC,dona emma,1,1,30.21
RJ,portela,1,1,229.9
RJ,penedo,1,1,89.9
MG,entre folhas,1,1,84.99
MG,engenheiro navarro,1,1,1997.0
MG,dom joaquim,1,1,149.0
MG,dom cavati,1,1,74.99
MG,divisa nova,1,1,689.9
GO,jaupaci,1,1,89.9
GO,jardim abc de goias,1,1,19.99
GO,jandaia,1,1,23.2
SC,guaraciaba,1,1,54.9
SC,galvao,1,1,59.5
SC,frei rogerio,1,1,99.9
SC,fragosos,1,1,99.99
GO,mutunopolis,1,1,24.41
GO,mossamedes,1,1,49.99
PB,paulista,1,1,475.6
PB,passagem,1,1,1199.0
PB,nova floresta,1,1,129.6
PB,montadas,1,1,84.99
PB,manaira,1,1,90.0
GO,flores de goias,1,1,24.99
GO,divinopolis de goias,1,1,79.0
GO,diorama,1,2,196.87
GO,itaguari,1,1,887.0
GO,ipiranga de goias,1,1,119.9
GO,hidrolandia,1,1,58.99
SC,iomere,1,1,49.0
GO,leopoldo de bulhoes,1,1,283.02
MG,delfim moreira,1,1,24.9
MG,datas,1,1,780.0
MG,cuite velho,1,1,19.99
RJ,laje do muriae,1,1,219.0
MG,felixlandia,1,1,75.0
MG,felisburgo,1,1,99.9
MG,felicio dos santos,1,1,169.9
MG,ewbank da camara,1,1,79.99
MG,estrela do sul,1,1,89.9
MG,estiva,1,1,10.9
MG,estevao de araujo,1,1,14.2
MG,glaura,1,1,69.9
MG,vitorinos,1,1,89.99
MG,virginia,1,1,35.9
PB,pirpirituba,1,1,1340.0
PB,pilar,1,1,58.99
PB,pianco,1,1,2200.0
PB,pedra lavrada,1,1,50.0
PB,pedra branca,1,1,44.99
SC,morro grande,1,1,119.8
GO,crominia,1,1,45.9
GO,cocalzinho de goias,1,1,149.9
GO,cezarina,1,1,13.49
GO,campos verdes,1,1,385.6
SC,monte castelo,1,1,78.0
SC,macieira,1,1,17.46
SC,lindoia do sul,1,1,103.9
SC,leoberto leal,1,1,24.99
SC,lajeado grande,1,1,130.0
SC,jose boiteux,1,1,119.69999999999999
GO,goiandira,1,1,94.9
GO,formoso,1,1,39.0
MG,divino das laranjeiras,1,1,35.9
RJ,mussurepe,1,1,99.99
RJ,macuco,1,1,69.9
GO,cabeceiras,1,1,14.9
MG,frei lagonegro,1,1,206.74
MG,frei gaspar,1,1,74.9
MG,fonseca,1,1,89.65
RJ,jamapara,1,1,32.0
RJ,jaguarembe,1,1,33.99
RJ,ibitioca,1,1,169.99
MG,guape,1,1,176.96
MG,grupiara,1,1,129.94
GO,buriti alegre,1,1,29.99
GO,britania,1,1,89.99
GO,bom jardim de goias,1,1,10.0
SC,paial,1,1,139.99
SC,ouro,1,1,278.79
SC,novo horizonte,1,1,74.9
SC,nossa senhora de caravaggio,1,1,120.0
PB,juru,1,1,890.0
PB,juripiranga,1,1,69.99
PB,jerico,1,1,75.0
PB,inga,1,1,130.0
PB,ibiara,1,1,278.0
PB,fagundes,1,1,198.9
PB,desterro,1,1,559.0
PB,curral de cima,1,1,199.0
SC,rio rufino,1,1,59.0
SC,rio dos cedros,1,1,49.9
SC,presidente nereu,1,1,52.99
SC,presidente castello branco,1,1,19.9
SC,ponte alta do norte,1,1,39.99
SC,picarras,1,1,155.0
SC,paraiso,1,1,79.9
GO,campinacu,1,1,179.9
GO,aragoiania,1,1,112.9
GO,apore,1,1,134.64
PE,sao joaquim do monte,1,1,79.0
PE,sao joao,1,1,427.0
PE,sao domingos,1,1,114.94
PE,sao benedito do sul,1,1,39.99
PE,santo antonio das queimadas,1,1,84.99
PE,santa terezinha,1,1,259.9
PE,santa filomena,1,1,160.0
MG,senhora dos remedios,1,1,29.99
MG,senador cortes,1,1,298.0
MG,senador amaral,1,2,179.46
MG,sardoa,1,1,119.9
PB,mae d'agua,1,1,39.89
PB,lucena,1,1,89.0
PB,lagoa,1,1,110.0
ES,ponto belo,1,1,79.9
GO,agua limpa,1,1,388.0
GO,agua fria de goias,1,1,152.0
GO,abadiania,1,1,949.99
ES,vargem grande do soturno,1,1,89.9
SC,sao cristovao do sul,1,1,118.99
SC,sao bonifacio,1,1,101.0
SC,sao bernardino,1,1,189.9
SC,santa terezinha,1,1,49.9
SC,santa rosa do sul,1,1,199.0
SC,santa cruz do timbo,1,1,30.99
SC,romelandia,1,1,159.99
GO,barro alto,1,1,97.9
GO,aurilandia,1,1,122.99
GO,aruana,1,2,144.8
GO,arenopolis,1,1,108.9
RJ,conrado,1,1,104.9
MG,ilicinea,1,1,89.9
MG,igaratinga,1,1,253.52
MG,ibiracatu,1,1,129.99
MG,ibertioga,1,1,162.5
MG,guiricema,1,1,149.9
MG,guinda,1,1,25.0
RJ,cambiasca,1,1,22.99
RJ,bom jesus do querendo,1,1,149.0
RJ,boa ventura,1,1,14.9
ES,sao joao do sobrado,1,1,55.92
ES,sao joao de petropolis,1,1,27.99
ES,santo antonio do canaa,1,1,160.0
ES,santa leopoldina,1,1,89.9
ES,quilometro 14 do mutum,1,1,49.9
ES,praia grande,1,1,59.9
SE,brejo grande,1,1,249.0
SE,aquidaba,1,1,89.0
SC,vargeao,1,1,499.9
ES,laranja da terra,1,1,69.9
SC,uniao do oeste,1,1,24.99
SC,tunapolis,1,1,315.39
SC,treviso,1,1,118.9
SC,tangara,1,1,354.9
ES,piacu,1,1,166.99
ES,paraju,1,1,79.9
ES,pancas,1,1,159.94
ES,pacotuba,1,1,50.9
ES,novo brasil,1,1,85.9
ES,mucurici,1,1,259.8
RJ,duas barras,1,1,14.89
RJ,corrego do ouro,1,1,28.9
SE,nossa senhora das dores,1,1,559.0
SE,neopolis,1,1,235.0
SE,monte alegre de sergipe,1,1,80.0
SE,malhador,1,1,23.99
SE,macambira,1,1,173.9
SE,japoata,1,1,179.9
SE,japaratuba,1,1,99.99
SE,itaporanga d'ajuda,1,1,159.99
SE,itabi,1,1,89.9
SE,indiaroba,1,1,48.0
SE,graccho cardoso,1,1,610.0
SE,general maynard,1,1,197.5
SE,cristinapolis,1,1,77.9
ES,ibiracu,1,1,27.3
ES,divino de sao lourenco,1,1,103.97
SE,campo do brito,1,1,76.8
SE,riachuelo,1,1,39.97
SE,poco redondo,1,1,419.8
RJ,boa esperanca,1,1,1399.99
RJ,bemposta,1,1,32.0
RJ,barao de juparana,1,1,28.49
MG,itabirinha,1,1,108.0
MG,ipuiuna,1,1,169.9
MG,ingai,1,1,96.0
MG,indianopolis,1,1,28.99
RJ,bacaxa,1,1,57.9
PR,xambre,1,2,511.0
PR,vitorino,1,1,49.0
PR,vitoria,1,1,28.99
SE,pirambu,1,1,289.0
SE,pinhao,1,1,420.0
SE,nossa senhora de lourdes,1,1,79.99
PB,barra de santa rosa,1,1,254.4
MS,coronel sapucaia,1,1,89.9
MS,corguinho,1,2,225.41
MS,caracol,1,1,94.0
MS,brasilandia,1,1,59.9
MS,bodoquena,1,2,428.0
SP,ajapi,1,1,108.0
SP,agisse,1,1,43.0
SE,telha,1,1,212.4
ES,brejetuba,1,1,128.89
ES,atilio vivacqua,1,1,89.9
ES,araguaia,1,1,49.0
ES,angelo frechiani,1,1,25.32
SE,sao miguel do aleixo,1,1,20.0
SE,santo amaro das brotas,1,1,19.9
SE,ribeiropolis,1,1,65.0
CE,vicosa do ceara,1,1,18.95
PR,vila reis,1,1,69.9
PR,tupassi,1,1,19.9
MG,itaguara,1,2,48.89
MG,jenipapo de minas,1,1,7.48
MG,japaraiba,1,1,108.9
MG,jampruca,1,1,235.9
MG,jaguaracu,1,1,55.9
MG,jaboticatubas,1,1,767.3
MG,itutinga,1,1,69.9
CE,uruburetama,1,1,58.99
PB,caldas brandao,1,1,139.0
PB,brejo dos santos,1,1,89.99
PB,brejo do cruz,1,1,1160.0
PB,bonito de santa fe,1,1,119.6
PB,belem,1,1,330.0
PE,tamandare,1,1,49.0
PE,siriji,1,1,39.99
MG,sao miguel do anta,1,1,173.59
MG,sao mateus de minas,1,1,59.88
MG,sao jose do divino,1,1,148.0
PE,sao vicente ferrer,1,1,169.99
PR,tamboara,1,1,8.99
SP,anhumas,1,1,58.99
SP,anhembi,1,1,106.9
SP,americo de campos,1,1,279.9
SP,alfredo marcondes,1,1,129.0
ES,aguia branca,1,1,12.9
DF,sobradinho,1,1,99.0
DF,santa maria,1,1,16.9
DF,guara,1,2,88.78999999999999
DF,ceilandia,1,1,49.9
PB,alagoa grande,1,1,139.99
PA,viseu,1,1,301.0
PA,ulianopolis,1,1,27.3
CE,saboeiro,1,1,163.99
CE,porteiras,1,1,16.55
CE,pires ferreira,1,1,18.95
CE,pindoretama,1,1,37.55
SP,aramina,1,1,97.9
SP,aparecida de monte alto,1,1,179.9
SP,aparecida d'oeste,1,1,19.9
CE,tururu,1,1,189.0
CE,taperuaba,1,1,55.49
CE,tabuleiro do norte,1,1,44.99
PR,teixeira soares,1,1,545.69
PE,terra nova,1,1,209.99
PE,terezinha,1,1,39.99
SP,balbinos,1,1,55.32
MS,bataipora,1,1,135.3
PB,assuncao,1,1,80.0
PR,sulina,1,1,29.9
PR,serra dos dourados,1,1,65.0
PR,sede alvorada,1,1,119.0
MG,lagoa dos patos,1,1,59.9
MG,joaima,1,1,37.9
MG,jequeri,1,1,655.0
PR,sao sebastiao da amoreira,1,1,45.0
PR,sao pedro do iguacu,1,1,117.3
PB,aroeiras,1,1,149.99
PB,areial,1,1,159.9
PB,araruna,1,1,129.9
PB,arara,1,1,109.9
PB,alagoa nova,1,1,113.0
CE,itapiuna,1,2,54.980000000000004
CE,itapage,1,1,159.99
CE,itaicaba,1,1,32.99
SP,botelho,1,1,189.98
SP,boraceia,1,1,29.0
SP,bora,1,1,119.9
CE,mombaca,1,1,219.9
CE,missi,1,1,109.9
CE,missao velha,1,1,14.99
CE,mauriti,1,1,14.9
CE,madalena,1,1,132.9
CE,palhano,1,1,99.0
CE,pacuja,1,1,339.95000000000005
CE,mucambo,1,1,119.9
SP,barao ataliba nogueira,1,1,1300.0
SP,bandeirantes d'oeste,1,1,49.99
CE,lages,1,1,59.0
CE,jucas,1,1,325.0
PR,sao miguel do cambui,1,1,59.9
PR,sao jose da boa vista,1,1,118.99
PR,sao jorge do oeste,1,1,34.9
PR,sao jorge do ivai,1,1,352.52
PR,sao jorge d'oeste,1,1,89.9
PR,sao clemente,1,1,139.8
PR,sao carlos do ivai,1,1,93.0
PR,santo inacio,1,1,65.9
PR,santo antonio do caiua,1,1,256.3
PR,santana do itarare,1,1,53.9
PR,santana,1,1,122.99
PR,santa margarida,1,1,49.9
CE,jaguaribara,1,1,98.0
CE,itarema,1,1,72.9
PR,santa lucia,1,1,48.9
MG,laranjal,1,1,289.0
MG,lamim,1,1,89.9
PR,santa cecilia do pavao,1,1,56.99
PR,santa amelia,1,1,160.0
PR,salto do itarare,1,1,259.9
PR,sabaudia,1,1,5.9
PR,rosario do ivai,1,1,29.0
PR,rio verde,1,1,159.9
CE,dourado,1,1,199.9
CE,croata,1,1,58.99
CE,ipaumirim,1,1,269.9
CE,independencia,1,1,110.0
CE,ibicuitinga,1,1,28.99
CE,guassusse,1,1,149.9
CE,lagoa do mato,1,1,35.99
MS,inocencia,1,1,36.9
MS,guia lopes da laguna,1,1,29.99
MS,gloria de dourados,1,1,45.8
SP,cipo-guacu,1,1,69.99
CE,coreau,1,1,29.99
CE,chorozinho,1,1,359.0
CE,chaval,1,1,150.0
CE,cedro,1,1,249.9
CE,caridade,1,1,99.9
CE,capistrano,1,1,35.0
SP,cassia dos coqueiros,1,1,74.9
CE,guaiuba,1,2,695.0
CE,groairas,1,1,152.15
CE,fortim,1,1,179.0
CE,flores,1,1,129.9
CE,erere,1,1,188.0
PR,reserva do iguacu,1,1,14.0
PR,rancho alegre d'oeste,1,1,117.3
PR,rancho alegre,1,1,89.9
PR,querencia do norte,1,1,79.9
PR,quatro pontes,1,1,149.0
MG,mamonas,1,1,230.0
MG,major porto,1,1,84.99
MG,macuco de minas,1,1,199.0
PR,pranchita,1,1,158.67
PR,porto rico,1,1,299.0
PR,planaltina do parana,1,1,10.75
PI,bertolinia,1,1,411.0
PA,tome-acu,1,1,24.99
PA,senador jose porfirio,1,1,6.0
PA,sao domingos do araguaia,1,1,227.0
PA,santo antonio do taua,1,1,32.9
SP,engenheiro balduino,1,1,179.6
SP,emilianopolis,1,2,169.85000000000002
SP,embauba,1,1,399.0
SP,elisiario,1,1,49.0
CE,aquiraz,1,1,370.0
CE,antonina do norte,1,1,76.8
CE,amontada,1,1,45.9
CE,amanari,1,1,390.0
CE,aiuaba,1,1,109.7
BA,wenceslau guimaraes,1,1,110.0
BA,wagner,1,1,119.9
CE,barreira,1,1,123.89
CE,banabuiu,1,1,79.0
CE,assare,1,1,81.0
CE,araripe,1,1,129.6
PA,tracuateua,1,1,13.98
BA,varzedo,1,1,39.9
BA,varzea nova,1,1,86.0
BA,varzea do poco,1,1,56.99
PI,baixa grande do ribeiro,1,1,159.99
PI,angical do piaui,1,1,29.99
PI,amarante,1,1,760.0
PI,alvorada do gurgueia,1,1,37.0
PI,alegrete do piaui,1,1,149.9
PE,xexeu,1,1,87.5
PE,vertentes,1,1,23.99
PE,triunfo,1,2,219.0
PE,tracunhaem,1,1,659.0
PR,pirapo,1,1,75.27
BA,umburanas,1,1,99.9
BA,ubata,1,1,144.0
SP,estrela d oeste,1,1,134.9
PR,perola independente,1,1,84.9
PR,perobal,1,1,80.0
PR,paula freitas,1,1,474.9
PR,paranapoema,1,1,89.99
MG,monsenhor paulo,1,1,53.99
MG,moema,1,1,189.99
MG,moeda,1,1,69.9
MG,miravania,1,1,35.0
BA,teodoro sampaio,1,1,64.9
BA,taboquinhas,1,1,289.0
SP,gabriel monteiro,1,1,34.9
SP,florinia,1,1,41.5
SP,flora rica,1,1,200.0
SP,fernao,1,1,29.0
SP,euclides da cunha paulista,1,2,163.25
SP,estrela d'oeste,1,1,227.07
BA,sao miguel das matas,1,1,169.94
BA,sao felix do coribe,1,1,226.0
BA,sao felix,1,1,27.9
SP,guarapua,1,1,60.0
MS,eldorado,1,1,25.9
PA,santa barbara do para,1,1,179.96
PA,rio maria,1,3,352.88
PA,picarra,1,1,1014.5999999999999
PA,pau d'arco,1,1,48.9
PA,ourem,1,1,31.9
PA,nova timboteua,1,1,99.9
PA,nova ipixuna,1,1,328.0
PA,nova esperanca do piria,1,1,2199.0
SP,galia,1,1,199.0
MG,martinesia,1,1,34.89
MG,marilac,1,1,657.8
MG,minduri,1,1,19.9
MG,mesquita,1,1,59.9
MG,mendonca,1,1,149.9
PR,palmital,1,1,179.0
PR,ouro verde do oeste,1,1,14.9
PR,ourizona,1,1,143.8
PR,novo itacolomi,1,1,90.0
PR,nova santa barbara,1,1,113.0
PR,nova laranjeiras,1,1,208.1
MG,morro vermelho,1,1,31.9
MG,morro do pilar,1,1,69.9
MG,morro do ferro,1,1,120.0
MG,morro da garca,1,1,199.0
BA,sento se,1,1,53.99
BA,saubara,1,1,179.9
BA,satiro dias,1,1,24.5
MS,paranhos,1,1,279.0
MS,paraiso das aguas,1,1,34.99
PA,juruti,1,1,49.9
BA,salinas da margarida,1,1,55.0
BA,ribeira do amparo,1,1,45.0
BA,riachao das neves,1,2,206.89000000000001
BA,retirolandia,1,1,89.9
SP,ibitiuva,1,1,14.9
SP,iaras,1,1,79.99
BA,sao desiderio,1,1,125.0
BA,santana do sobrado,1,1,36.9
BA,santa brigida,1,1,84.9
BA,salobro,1,1,72.2
SP,guzolandia,1,1,101.62
SP,guatapara,1,1,75.0
MG,miradouro,1,1,49.9
PR,mato rico,1,1,72.9
MG,orizania,1,1,129.95
MG,olhos d'agua,1,1,99.9
MG,olaria,1,1,79.9
MG,nova resende,1,1,10.99
MG,natercia,1,1,39.9
MG,nacip raydan,1,1,74.9
PA,murucupi,1,1,129.9
PA,morada nova,1,1,59.99
PA,monte alegre,1,1,98.0
PA,mocajuba,1,1,59.9
PA,medicilandia,1,1,8.99
MS,ribas do rio pardo,1,1,47.9
MS,prudencio thomaz,1,1,32.99
MS,porto murtinho,1,1,55.0
MS,pedro gomes,1,1,113.0
PR,manfrinopolis,1,1,111.0
PR,mandirituba,1,1,12.67
MG,palmopolis,1,1,89.99
MG,paineiras,1,1,58.99
MG,padre paraiso,1,1,59.9
MG,padre carvalho,1,1,563.0
BA,nova vicosa,1,1,205.99
SP,itaoca,1,1,55.8
BA,presidente janio quadros,1,1,149.9
BA,ponto novo,1,1,360.0
BA,planalto,1,1,91.0
BA,planaltino,1,1,191.8
BA,pirai do norte,1,1,29.49
SP,irape,1,2,379.98
PR,nova esperanca do sudoeste,1,1,84.99
PR,nova america da colina,1,1,58.99
SP,jeriquara,1,1,129.0
BA,nova redencao,1,1,19.9
BA,nova fatima,1,1,143.8
BA,muritiba,1,1,159.49
BA,mundo novo,1,1,129.0
BA,mucuge,1,1,256.99
BA,morro de sao paulo,1,1,691.96
BA,monte santo,1,1,23.21
BA,monte gordo,1,1,199.9
SP,jamaica,1,1,59.0
BA,pedrao,1,1,325.0
BA,pau brasil,1,1,239.2
PR,mariopolis,1,1,154.99
PR,marilena,1,1,89.99
PR,marilandia do sul,1,1,159.9
PR,mariental,1,1,1799.0
PR,laranjal,1,1,27.99
PR,jussara,1,1,29.49
MG,pedra menina,1,1,23.4
MG,pedra do indaia,1,1,72.99
MG,pavao,1,1,60.0
MG,paula candido,1,1,129.0
MG,patis,1,1,49.9
MG,passa tempo,1,1,120.0
MG,sao goncalo do rio das pedras,1,1,169.0
PA,jacareacanga,1,1,49.0
PA,itupiranga,1,1,399.0
PA,igarape-miri,1,1,27.99
PA,igarape-acu,1,1,69.0
PA,floresta do araguaia,1,1,129.99
PA,curralinho,1,1,188.76
PA,breves,1,1,609.0
PA,aurora do para,1,1,78.0
SP,macaubal,1,1,89.8
BA,lagoa real,1,1,410.0
BA,jussiape,1,1,37.0
BA,joao dourado,1,1,19.9
BA,jiquirica,1,1,499.99
BA,jaua,1,1,149.9
BA,jandaira,1,1,59.99
BA,jacuipe,1,1,13.98
SP,lutecia,1,1,887.0
SP,lavrinhas,1,1,599.9
BA,mansidao,1,1,49.0
BA,maiquinique,1,1,119.4
BA,lencois,1,1,218.0
BA,lamarao,1,1,59.0
PR,leopolis,1,1,18.9
BA,itanhem,1,1,230.0
BA,itamira,1,2,55.9
MG,sao geraldo do baguari,1,1,117.3
PI,demerval lobao,1,1,15.0
PI,conceicao do caninde,1,1,155.44
PI,caxingo,1,1,29.0
PI,canto do buriti,1,1,599.5
PI,campo grande do piaui,1,1,155.99
PI,campo alegre do fidalgo,1,1,194.98
PI,caldeirao grande do piaui,1,1,110.0
PI,bocaina,1,1,114.9
PR,jardim olinda,1,1,139.0
MS,vicentina,1,1,189.9
MS,terenos,1,1,62.89
MS,tacuru,1,1,120.0
MS,sanga puita,1,1,36.9
BA,itaju do colonia,1,1,39.9
BA,itaguacu da bahia,1,1,249.7
BA,itagimirim,1,1,129.9
MG,pirajuba,1,1,135.9
MG,piracema,1,1,149.0
MG,pinhotiba,1,1,59.9
MG,pingo-d'agua,1,1,369.48
MG,pescador,1,1,29.9
MG,pequi,1,1,169.99
PR,itambe,1,1,269.9
PR,iretama,1,1,117.3
BA,ipupiara,1,1,495.0
SP,mira estrela,1,1,198.0
SP,meridiano,1,1,119.0
BA,itape,1,1,230.0
BA,itaparica,1,1,168.49
SP,nova independencia,1,1,23.9
SP,nova guataporanga,1,1,75.0
PR,ilha dos valadares,1,1,67.99
PR,iguatu,1,1,137.9
PR,iguaracu,1,2,525.7
PR,icaraima,1,1,27.9
PR,ibema,1,1,134.9
PR,guaraquecaba,1,1,49.9
PR,guapirama,1,1,89.9
PR,guamiranga,1,1,214.0
PR,guairaca,1,1,63.8
MG,ponto do marambaia,1,1,13.7
MG,pocoes de paineiras,1,1,102.89000000000001
SP,natividade da serra,1,1,125.0
SP,nantes,1,1,79.0
SP,monte castelo,1,1,91.5
BA,gongogi,1,1,29.99
BA,gentio do ouro,1,1,98.7
SP,palmeira d oeste,1,1,49.9
SP,palmares paulista,1,1,59.9
SP,onda verde,1,1,69.81
BA,ipecaeta,1,1,23.4
BA,igrapiuna,1,1,29.99
BA,igapora,1,1,39.99
BA,ibitita,1,1,1450.0
BA,ibitira,1,1,399.0
BA,ibitiara,1,1,118.9
BA,ibirapua,1,1,122.99
BA,ibiraja,1,2,277.95
SP,oleo,1,1,59.9
SP,novais,1,1,99.9
SP,nova luzitania,1,1,22.9
SP,pardinho,1,1,272.8
PR,godoy moreira,1,1,1049.0
PR,foz do jordao,1,1,49.0
PR,formosa do oeste,1,1,69.9
PR,florida,1,1,69.9
PR,fenix,1,1,44.99
MG,queixada,1,1,59.0
MG,quatituba,1,1,105.0
MG,prudente de morais,1,2,139.0
MG,pratapolis,1,1,49.99
PI,joaquim pires,1,1,12.97
BA,ibipeba,1,1,61.7
BA,ibiajara,1,1,45.0
BA,humildes,1,1,249.99
BA,heliopolis,1,1,149.0
BA,governador mangabeira,1,1,98.0
PI,ilha grande,1,1,139.9
PI,gilbues,1,1,296.0
PI,francisco santos,1,1,20.9
MG,sao joao da ponte,1,1,461.84
PR,farol,1,1,126.99
PR,doutor ulysses,1,1,122.0
PR,doutor camargo,1,1,211.05
PR,douradina,1,1,99.9
MT,vila bela da santissima trindade,1,1,29.99
MT,uniao do sul,1,1,220.7
MT,tapurah,1,1,125.0
MT,bom jesus do araguaia,1,1,1199.9
MT,sao jose do xingu,1,1,49.3
MT,sao felix do araguaia,1,1,98.8
SP,paulistania,1,1,99.0
SP,parisi,1,1,34.49
BA,cotegipe,1,1,84.99
BA,cordeiros,1,1,322.75
BA,coracao de maria,1,1,279.9
BA,condeuba,1,1,56.99
BA,conceicao do almeida,1,1,99.0
BA,cocos,1,1,49.99
SP,piacatu,1,1,51.19
SP,pereiras,1,1,54.99
SP,pedranopolis,1,1,59.9
BA,filadelfia,1,1,79.9
BA,erico cardoso,1,1,8.09
BA,dom macedo costa,1,1,55.9
BA,dias d avila,1,1,45.0
PI,itaueira,1,2,105.28
PI,isaias coelho,1,1,170.0
PI,inhuma,1,1,78.0
PR,cruzeiro do iguacu,1,1,129.99
PR,corumbatai do sul,1,1,27.49
PR,coronel domingos soares,1,1,89.0
PR,contenda,1,1,89.9
PR,conselheiro mairinck,1,1,67.0
MG,rio espera,1,1,149.9
MG,rio doce,1,1,66.0
MG,ribeiro junqueira,1,1,149.0
MG,ressaquinha,1,1,189.9
BA,carnaiba do sertao,1,1,54.98
BA,caraibas,1,1,235.9
BA,capela do alto alegre,1,1,39.99
SP,planalto,1,1,69.99
SP,piquerobi,1,1,85.0
SP,pinheiros,1,1,199.99
BA,cravolandia,1,1,139.9
SP,queiroz,1,1,45.0
BA,canudos,1,1,174.9
BA,candeal,1,1,144.99
BA,canarana,1,1,107.9
BA,canapolis,1,1,13.65
BA,campo alegre de lourdes,1,1,99.99
BA,caldas do jorro,1,1,370.0
BA,cairu,1,1,58.99
SP,populina,1,1,47.6
SP,pontes gestal,1,1,89.99
BA,cipo,1,1,179.0
BA,chorrocho,1,1,49.9
BA,central,1,1,119.5
BA,caturama,1,1,19.99
PR,doce grande,1,1,49.49
PR,diamante d'oeste,1,1,289.9
BA,caem,1,1,57.9
BA,cabaceiras do paraguacu,1,1,31.9
MG,ravena,1,1,69.99
PR,candoi,1,1,43.0
PR,campo magro,1,1,39.8
MG,rubelita,1,1,57.89
MG,santa rita do itueto,1,1,59.9
MG,santa rita de jacutinga,1,1,29.99
MG,santa maria do salto,1,1,38.0
PI,redencao do gurgueia,1,1,179.8
BA,brotas de macaubas,1,1,168.0
BA,brejolandia,1,1,13.98
BA,brejoes,1,1,124.9
BA,botupora,1,1,325.0
BA,boquira,1,1,69.9
SP,redencao da serra,1,1,89.9
PI,pedro ii,1,1,74.9
PI,nova santa rita,1,1,13.98
PI,matias olimpio,1,1,600.0
PI,marcos parente,1,1,13.65
PI,luis correia,1,1,115.0
PI,lagoinha do piaui,1,1,115.0
PI,lagoa do piaui,1,1,84.99
PI,lagoa de sao francisco,1,1,68.99
MG,santa fe de minas,1,1,159.9
PR,campo do tenente,1,1,55.9
MT,santo antonio do leste,1,1,149.0
MT,ribeirao cascalheira,1,1,29.9
MT,itanhanga,1,1,69.99
MT,ipiranga do norte,1,1,95.0
MT,feliz natal,1,1,259.99
MT,curvelandia,1,1,189.0
BA,andarai,1,1,79.9
SP,santa salete,1,1,81.99
SP,santa clara d'oeste,1,1,99.99
BA,biritinga,1,1,120.0
BA,belmonte,1,1,37.99
BA,barrocas,1,1,99.99
BA,barro preto,1,1,118.8
BA,barra do tarrachil,1,3,272.9
BA,banzae,1,1,99.99
BA,baixa grande,1,1,44.0
SP,salto grande,1,1,640.0
SP,rubineia,1,1,100.0
SP,riversul,1,1,89.9
SP,rincao,1,1,79.0
MT,santo antonio do leverger,1,1,97.0
PI,pio ix,1,1,149.99
BA,arataca,1,1,795.0
BA,aramari,1,2,167.4
PR,bom sucesso,1,1,89.9
PR,bom jesus do sul,1,1,199.9
PR,boa esperanca do iguacu,1,1,35.9
PR,boa esperanca,1,1,129.0
PR,barracao,1,1,19.99
PR,barra do jacare,1,1,57.9
PR,balsa nova,1,1,19.45
MG,santo antonio do aventureiro,1,1,77.99
BA,aracatu,1,1,75.99
BA,apuarema,1,1,169.99
BA,apora,1,1,44.9
BA,antonio goncalves,1,1,34.9
BA,anguera,1,1,99.0
BA,angical,1,1,269.9
MT,nova lacerda,1,1,339.74
MT,nova guarita,1,1,25.0
MT,nortelandia,1,1,174.9
BA,anage,1,1,63.8
BA,america dourada,1,1,169.9
BA,amargosa,1,1,54.99
BA,adustina,1,1,74.8
BA,acajutiba,1,1,28.89
BA,abrantes,1,1,139.0
AP,vitoria do jari,1,1,85.95
AP,porto grande,1,1,29.99
AP,oiapoque,1,1,385.0
SP,santo expedito,1,1,280.0
SP,santo antonio do aracangua,1,1,1099.0
BA,arraial d ajuda,1,1,72.62
BA,aribice,1,1,42.0
MG,santana do deserto,1,1,190.9
MG,santana do capivari,1,1,25.0
MG,santana de pirapama,1,1,49.9
PR,alto sao joao,1,1,54.99
PR,alto piquiri,1,1,412.0
PR,alto paraiso,1,1,56.99
PR,alto alegre do iguacu,1,2,74.69999999999999
PR,alexandra,1,1,31.9
PR,adrianopolis,1,1,73.9
MG,sao geraldo da piedade,1,1,139.8
MG,sao francisco do gloria,1,1,69.9
MT,conquista d'oeste,1,1,89.99
MT,porto estrela,1,1,129.9
MT,porto alegre do norte,1,1,410.0
MT,novo mundo,1,1,59.15
MT,nova ubirata,1,1,99.9
AL,passo de camaragibe,1,1,41.98
AL,paripueira,1,1,349.9
SP,tapinas,1,1,89.99
SP,taiacu,1,1,60.5
SP,suzanapolis,1,1,76.9
SP,serra azul,1,1,72.5
SP,sarutaia,1,1,59.9
SP,sao sebastiao da serra,1,1,157.9
AM,itacoatiara,1,1,57.98
AM,coari,1,1,1190.65
AL,vicosa,1,1,21.9
AL,uniao dos palmares,1,1,259.99
AL,traipu,1,1,42.99
AL,taquarana,1,1,146.99
AL,tanque d'arca,1,2,578.0
AL,sao sebastiao,1,1,2159.98
MG,sao felix de minas,1,1,388.9
MG,sao domingos das dores,1,1,59.9
MG,sao domingos,1,1,59.9
MG,sao bento abade,1,1,16.0
MG,sao benedito,1,1,52.64
MG,santo hipolito,1,1,104.4
MG,santo antonio dos campos,1,1,159.0
MG,santo antonio do rio abaixo,1,1,6.0
PR,adhemar de barros,1,1,139.0
PI,varzea grande,1,1,12.5
PI,uniao,1,1,329.0
PI,simplicio mendes,1,1,16.6
PI,sebastiao leal,1,1,24.99
AL,santa luzia do norte,1,1,23.8
AL,porto de pedras,1,1,179.9
AL,piacabucu,1,2,228.9
SP,tuiuti,1,1,49.0
AL,novo lino,1,1,79.9
AL,murici,1,1,49.9
AL,monteiropolis,1,1,159.9
AL,matriz de camaragibe,1,1,64.0
AL,maribondo,1,1,49.9
AL,marechal deodoro,1,1,349.9
AL,mar vermelho,1,2,519.98
AL,luziapolis,1,1,129.99
AL,lagoa da canoa,1,1,160.99
SP,trabiju,1,1,259.99
SP,termas de ibira,1,1,71.9
SP,tecainda,1,1,149.99
AL,sao jose da tapera,1,1,109.9
AL,sao bras,1,1,29.9
AL,santana do ipanema,1,1,249.9
MT,nobres,1,1,41.99
TO,novo alegre,1,1,279.99
TO,nova olinda,1,1,29.9
TO,natividade,1,1,349.9
MT,itiquira,1,1,133.0
TO,sitio novo do tocantins,1,2,314.9
TO,silvanopolis,1,1,229.99
TO,sandolandia,1,1,799.0
TO,pugmil,1,1,114.9
TO,praia norte,1,1,79.0
TO,pium,1,1,20.0
TO,pequizeiro,1,1,219.99
TO,peixe,1,1,89.99
TO,augustinopolis,1,1,107.0
TO,arapoema,1,1,55.9
TO,araguacu,1,1,129.5
MG,cachoeira do brumado,1,1,195.9
RS,aratiba,1,1,92.5
RS,andre da rocha,1,1,119.0
RS,alto alegre,1,1,139.9
RS,alpestre,1,1,118.9
RS,almirante tamandare do sul,1,1,49.9
RS,alegria,1,1,39.9
TO,lajeado,1,1,120.0
AL,coite do noia,1,1,89.9
AL,canapi,1,1,230.0
AL,campo alegre,1,2,919.1
AL,cajueiro,1,1,99.9
TO,combinado,1,1,29.0
TO,centenario,1,1,134.99
TO,carmolandia,1,1,129.0
TO,buriti do tocantins,1,1,59.9


Monthly purchasing trends:
purchase_month,orders,item_revenue,freight_total
2016-09,1,134.97,8.49
2016-10,265,40325.11,6165.55
2016-12,1,10.9,8.72
2017-01,750,111798.36,15684.01
2017-02,1653,234223.4,37015.92
2017-03,2546,359198.85,55132.1
2017-04,2303,340669.68,50142.72
2017-05,3546,489338.25,77513.15
2017-06,3135,421923.37,68127.0
2017-07,3872,481604.52,84694.56
2017-08,4193,554699.7,91132.66
2017-09,4150,607399.67,93677.82
2017-10,4478,648247.65,102869.36
2017-11,7289,987765.37,165598.83
2017-12,5513,726033.1900000001,117045.1
2018-01,7069,924645.0,153242.46
2018-02,6555,826437.13,139731.28
2018-03,7003,953356.25,167241.99
2018-04,6798,973534.09,159344.84
2018-05,6749,977544.6900000001,151229.83
2018-06,6099,856077.86,155900.43
2018-07,6159,867953.46,159853.82
2018-08,6351,838576.64,146915.0


5. Outline an RFM segmentation approach if the available data supports it.

RFM (Recency, Frequency, Monetary Value) segmentation will be used to classify customers according to their purchasing behavior and value to the business.

Implementation Approach:

* Join the customer, orders, and order-items datasets using customer_id and order_id.

* Select eligible orders, such as delivered orders, and document the chosen order-status criteria.

* Aggregate order-item values to the order level to avoid double-counting orders.

* Group the eligible orders by customer_unique_id.

* Calculate Recency, Frequency, and Monetary Value for every customer.

* Assign scores from 1 to 5 to each metric using quantile-based scoring. A lower recency value receives a higher score, while higher frequency and monetary values receive higher scores.

* Combine the three scores to create an RFM score and classify customers into meaningful segments.

The scoring logic is:
- Recency: Rank recency in descending order so fewer days since the last purchase earns a higher score.
- Frequency: Rank purchase counts in ascending order so more purchases earn a higher score.
- Monetary: Rank total spending in ascending order so greater spending earns a higher score.
- Ties: Use rank(method="average", pct=True) so identical metric values share the same percentile and score.
- Score conversion: Multiply the percentile rank by 5, round upward, and constrain the result to the range 1–5.

Summary on RFM segment:
segment,customers,monetary_total,mean_frequency,mean_recency_days
Needs Attention,54165,7412973.88,1.0,134.0175205390935
At Risk,37389,5328881.99,1.0288320094145338,394.95627056086016
Champions,931,305122.29,2.189044038668099,89.2717508055854
Loyal,873,174519.95,2.071019473081329,177.22794959908362

