<map version="freeplane 1.3.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="cloudmesh" ID="ID_1723255651" CREATED="1283093380553" MODIFIED="1439995817998"><hook NAME="MapStyle">

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node">
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right">
<stylenode LOCALIZED_TEXT="default" MAX_WIDTH="600" COLOR="#000000" STYLE="as_parent">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="10"/>
<node TEXT="API" POSITION="left" ID="ID_159876332" CREATED="1439934735041" MODIFIED="1439934738497">
<edge COLOR="#00ff00"/>
<node TEXT="keys" ID="ID_1568571895" CREATED="1439934812949" MODIFIED="1439995961805">
<icon BUILTIN="button_ok"/>
<node TEXT="ssh" ID="ID_1407690079" CREATED="1439935610306" MODIFIED="1439995953471">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="openstack" ID="ID_1779213754" CREATED="1439935617170" MODIFIED="1439995956052">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="git" ID="ID_1035196855" CREATED="1439935622670" MODIFIED="1439995958822">
<icon BUILTIN="button_ok"/>
</node>
</node>
<node TEXT="common" ID="ID_362026122" CREATED="1439934739872" MODIFIED="1439996373769">
<icon BUILTIN="bookmark"/>
<node TEXT="ConfigDict" ID="ID_804057634" CREATED="1439934791631" MODIFIED="1439995968908">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="FlatDict" ID="ID_1489787187" CREATED="1439934831533" MODIFIED="1439996331504">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="DictDB" ID="ID_1233027001" CREATED="1439934851537" MODIFIED="1439996334154">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Tables" ID="ID_669366295" CREATED="1439934876483" MODIFIED="1439996336813">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Types" ID="ID_897735641" CREATED="1439934886210" MODIFIED="1439996339194">
<icon BUILTIN="bookmark"/>
</node>
</node>
<node TEXT="mesh" ID="ID_1022198027" CREATED="1439993783617" MODIFIED="1439993787123">
<node TEXT="iaas" ID="ID_489486367" CREATED="1439934801214" MODIFIED="1439935653145">
<node TEXT="Provider" ID="ID_737648708" CREATED="1439935654128" MODIFIED="1439935662825">
<node TEXT="libcloud (deprecated)" ID="ID_1641668422" CREATED="1439935666313" MODIFIED="1439995945450">
<icon BUILTIN="button_cancel"/>
</node>
<node TEXT="OpenStack (API)" ID="ID_982040791" CREATED="1439993299424" MODIFIED="1439996321759">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Azure" ID="ID_251096150" CREATED="1439993318683" MODIFIED="1439993328187"/>
<node TEXT="AWS" ID="ID_546509942" CREATED="1439993328755" MODIFIED="1439993331880"/>
<node TEXT="KVM/LXC (Comet)" ID="ID_912704480" CREATED="1439993348842" MODIFIED="1439996318701">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Docker" ID="ID_357451971" CREATED="1439996285215" MODIFIED="1439996325430">
<icon BUILTIN="bookmark"/>
</node>
</node>
</node>
<node TEXT="cloud" ID="ID_746237386" CREATED="1439935798992" MODIFIED="1439935804204">
<node TEXT="register" ID="ID_1517118598" CREATED="1439935805147" MODIFIED="1439996479590">
<icon BUILTIN="bookmark"/>
<icon BUILTIN="help"/>
<node TEXT="cloudmesh.yaml" ID="ID_1912466515" CREATED="1439996034767" MODIFIED="1439996346781">
<icon BUILTIN="button_ok"/>
</node>
</node>
<node TEXT="mesh" ID="ID_494440704" CREATED="1439935859322" MODIFIED="1439996469038">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="default" ID="ID_1810614609" CREATED="1439935869074" MODIFIED="1439996487055">
<icon BUILTIN="bookmark"/>
<icon BUILTIN="help"/>
</node>
</node>
</node>
<node TEXT="launcher" ID="ID_37366969" CREATED="1439996170051" MODIFIED="1439996174883">
<node TEXT="SLURM" ID="ID_56400494" CREATED="1439996176202" MODIFIED="1439996429401">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Hadoop" ID="ID_1017415204" CREATED="1439996189056" MODIFIED="1439996194104"/>
<node TEXT="kubernetes" ID="ID_207614421" CREATED="1439996195456" MODIFIED="1439996432780">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Machine Learning&#xa;Virtual Cluster" ID="ID_1862618026" CREATED="1439996234873" MODIFIED="1439996436384">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Mesos" ID="ID_1169028807" CREATED="1439996253135" MODIFIED="1439996264352"/>
</node>
</node>
<node TEXT="commands" POSITION="left" ID="ID_1965732118" CREATED="1439935725779" MODIFIED="1439935735191">
<edge COLOR="#ff00ff"/>
<node TEXT="nova" ID="ID_1648867650" CREATED="1439935736894" MODIFIED="1439996359109">
<icon BUILTIN="button_ok"/>
</node>
<node TEXT="vm" ID="ID_1966355938" CREATED="1439993752756" MODIFIED="1439996443238">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="list" ID="ID_1176904302" CREATED="1439993860034" MODIFIED="1439996445908">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="image" ID="ID_1231224767" CREATED="1439993866201" MODIFIED="1439996448954">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="flavor" ID="ID_47883411" CREATED="1439993876149" MODIFIED="1439996452752">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="register" ID="ID_919299477" CREATED="1439993902496" MODIFIED="1439996455934">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="activate" ID="ID_1178798733" CREATED="1439993915183" MODIFIED="1439996459090">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="default" ID="ID_1494681741" CREATED="1439993983822" MODIFIED="1439996461930">
<icon BUILTIN="bookmark"/>
</node>
</node>
<node TEXT="Targeted&#xa;Public Clouds" POSITION="right" ID="ID_1596585255" CREATED="1439993391966" MODIFIED="1439995817997">
<edge COLOR="#00ffff"/>
<node TEXT="FutureSystems" ID="ID_534211824" CREATED="1439993430472" MODIFIED="1439993438567">
<node TEXT="OpenStack" ID="ID_1102122320" CREATED="1439993439248" MODIFIED="1439996416165">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Baremetal" ID="ID_291335981" CREATED="1439993447819" MODIFIED="1439993456174"/>
<node TEXT="HPC/Slurm" ID="ID_1714229526" CREATED="1439993457799" MODIFIED="1439993465854"/>
</node>
<node TEXT="AWS" ID="ID_730960873" CREATED="1439993469749" MODIFIED="1439993476014"/>
<node TEXT="Azure" ID="ID_1251109021" CREATED="1439993477326" MODIFIED="1439993480246"/>
<node TEXT="XSEDE" ID="ID_1232621256" CREATED="1439993483228" MODIFIED="1439993490645">
<node TEXT="Comet" ID="ID_398286879" CREATED="1439993491338" MODIFIED="1439996420035">
<icon BUILTIN="bookmark"/>
</node>
</node>
</node>
<node TEXT="Interfaces" POSITION="right" ID="ID_705638582" CREATED="1439993556167" MODIFIED="1439993569331">
<edge COLOR="#7c0000"/>
<node TEXT="REST" ID="ID_1955365963" CREATED="1439934681882" MODIFIED="1439993584583"/>
<node TEXT="command" ID="ID_1350540027" CREATED="1439934688753" MODIFIED="1439993587860">
<node TEXT="shell" ID="ID_1767036000" CREATED="1439934698065" MODIFIED="1439996399750">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="line" ID="ID_1785949012" CREATED="1439934704743" MODIFIED="1439996402866">
<icon BUILTIN="bookmark"/>
</node>
</node>
</node>
<node TEXT="Documentation" POSITION="right" ID="ID_1956683119" CREATED="1439995657874" MODIFIED="1439995666580">
<edge COLOR="#7c007c"/>
<node TEXT="Pycharm Inspect Code" ID="ID_1890213346" CREATED="1439995667324" MODIFIED="1439996370702">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Manual" ID="ID_527047828" CREATED="1439995688459" MODIFIED="1439995700611">
<node TEXT="Install" ID="ID_351234514" CREATED="1439995701283" MODIFIED="1439995705067">
<node TEXT="Windows" ID="ID_1166167413" CREATED="1439995705936" MODIFIED="1439996377393">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="Linux" ID="ID_25084056" CREATED="1439995710842" MODIFIED="1439996380372">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="OSX" ID="ID_1541560727" CREATED="1439995715426" MODIFIED="1439996383894">
<icon BUILTIN="bookmark"/>
</node>
</node>
<node TEXT="API" ID="ID_1418562298" CREATED="1439995722170" MODIFIED="1439996387756">
<icon BUILTIN="bookmark"/>
</node>
<node TEXT="command shell/line" ID="ID_1796455198" CREATED="1439995735087" MODIFIED="1439996390928">
<icon BUILTIN="bookmark"/>
</node>
</node>
</node>
</node>
</map>
