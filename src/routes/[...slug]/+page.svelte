<script lang="ts">
import { Frag, Img, Imgfrag, Code, Notes, RevealJsContext, Slide } from '$lib';
import 'reveal.js/dist/theme/black.css';
import 'reveal.js/plugin/highlight/monokai.css';

import UnoUno  from '../galleries/1-1.svelte';
import UnoDue  from '../galleries/1-2.svelte';
import UnoTre  from '../galleries/1-3.svelte';
import UnoQuatro  from '../galleries/1-4.svelte';
import DueUno  from '../galleries/2-1.svelte';
import DueTre  from '../galleries/2-3.svelte';
import SDtrain  from '../galleries/sd-train.svelte';

const interval = 5000;
</script>
<style>
    .container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 1fr 1fr;
        height: 100vh; /* Set the container height to full viewport height */
    }
    
    .box {
        /* border: 1px solid #000; */
        box-sizing: border-box;
        display: block; /* flex */
        /* justify-content: center;
        align-items: center; */
        font-size: 24px;
    }
    .par {
        font-size: xx-large;
    }
		.green {
			color: #43b719;
		}
		.yellow {
			color: #b5b515;
		}		
</style>
<!-- a container with fixed size is required -->

	<Slide>
		<h2>
			Arte e creatività 
		</h2>
		<h2>
			nell'era dell'intelligenza artificiale
		</h2>
		<img class="r-frame"  
		data-src="/sd/control-net/Odifreddi-spazio.png" alt="">
		<p>Eli Spizzichino e Piergiorgio Odifreddi </p>
		<p class="par">
			generative AI con le opere di Aldo Spizzichino
		</p>	
	</Slide>
	
	<Slide>
		<h2>
			Di cosa si parlerà oggi
		</h2>
		<p class="fragment fade-right">Prima parte</p>
		<ul style="width: 100vh;">
			<li class="fragment fade-right"> Cos'è la Generative AI</li>
			<li class="fragment fade-right"> Creatività biologica</li>
			<li class="fragment fade-right"> Analogie apprendimento animale e artificiale</li>
			<li class="fragment fade-right"> Creatività biologica</li>
			<li class="fragment fade-right"> Creatività artificiale (come funzionano le Neural networks)</li>
			<li class="fragment fade-right"> Criticità dei modelli di ML</li>
		</ul>
		<p class="fragment fade-right">Seconda parte</p>
		<ul style="width: 100vh;">
			<li class="fragment fade-right"> Le opere di Aldo Spizzichino</li>
			<li class="fragment fade-right"> Copiare lo stile</li>
			<li class="fragment fade-right"> Re-immaginare con quello stile</li>
			<li class="fragment fade-right"> Live Demo</li>
		</ul>
		<p class="fragment fade-right">Terza parte</p>
		<ul style="width: 100vh;">
			<li class="fragment fade-right"> Come cambia il lavoro per gli artisti del presente</li>
			<li class="fragment fade-right"> Opere derivate e copyrights</li>
			<li class="fragment fade-right"> Conclusioni</li>
		</ul>
	</Slide>
	<Slide>
		<h2>
			Generative AI? 
		</h2>
		<div class="container fragment" style="margin-top: -30px;">
			<div class="box">
				<p>Generazioni di immagini</p>
				<Img src="/2/polyfreddi.png" class_="" width="800px"/>
			</div>
			<div class="box">
				<p>Generazioni di testo</p>
				<p class="green">Perché i ricercatori scientifici sono bravi a fare feste?</p>
				<p class="yellow">Perché sanno come mescolare bene le soluzioni!</p>
				<br>
				<p class="green">Come si chiama il ricercatore che ha paura del buio?</p>
				<p class="yellow">Un fotone!</p>
				
			</div>
			<div class="box">
				<p>Composizione di musica</p>
				<p class="green">MuseNet improvises Chopin from Mozart’s Rondo alla Turca</p>
				<audio controls data-autoplay src="/MuseNet.mp3"></audio>
			</div>
			<div class="box">
				<p>e tanto altro ancora..</p>
			</div>
		</div>
		
		
		<Notes>	
			<p>Esempi con delle immagini divertenti, e chiedere al pubblico quanti l'hanno provata</p>
			<p>Spiegare le differenze applicazioni della Generative AI</p>
		</Notes>		

	</Slide>
	<Slide>
		<h2>Creatività biologica</h2>
		<Slide>
			<Frag>Io non sono creativo...</Frag>
			<Imgfrag src="/2/casa-1.png" height="60vh"></Imgfrag>
			<Notes>

			<p>Arg: io non sono creativo... </p>
			<p>Siamo sicuramente la specie più creativa, anche solo il fatto che ci troviamo qui e parliamo di queste cose dimostra la ns innata creatività (paragoni con altri animali)
			</p>
			<p>Spesso questa affermazione viene dal fatto, che non si hanno gli strumenti per esprimere la propria creatività, ma di base siamo tutti creativi, 
				e vedremo come IA ha abbassato la barriera di entrata per molti che non si considerano creativi</p>

			</Notes>		
		</Slide>
		<Slide>
			<DueUno interval={5000} />
			<Notes>
	<p>Viene da chiedersi qual'è il sw cognitivo in funzione nel ns cervello che assorbe le idee, le sminuzza e le processa continuamente creando nuove idee</p>
	<p>Per molti anni, gli scienziati hanno cercato di capire questi meccanismi della mente, in quanto era evidente che  un moscerino era più capace di un computer digitale in certi compiti. Questo ha portato l'attenzione ad un problema architetturale: i programmi tradizionali processano i dati i maniera sequenziale, non c'è nessuna incertezza, ambiguità o capacità discrezionale</p>
	<p>Il cervello degli animali, invece, anche lavorando a frequenze molto più lente, sono in grado di processare gli input in parallelo, e l'ambiguità è una caratteristica della capacità di calcolo</p>

	<p>C'è poi il mito dell'emisfero destro/sinistro con una parte deputata al pensiero più razionale e l'altra più creativa. In realtà i neuroscienziati hanno visto che le persone più creative usano davvero entrambi gli emisferi del cervello</p>
	<p>alcune parti, come il linguaggio è vero che sono concentrate nella parte SX, ma per la "creatività" è necessario l'interazione di più parti del cervello per risolvere un determinato compito, 	quindi si parla di Rete Cerebrali. 
	</p>
			</Notes>		
		</Slide>
		<Slide>
		<p class="par">	reti coinvolte nel processo di creatività</p>
			<Imgfrag src="/2/2/BRAIN-NET.png" width={"700px"}></Imgfrag>

			<Notes>

	<p>Ci sono tre reti principali che interagiscono nel processo di creatività, in qualsiasi campo lo si applichi, scienza, arte...:</p>
	<p>Executive attention network (plan mode), ci permette di tenere più cose in testa contemporaneamente, una sorta di memoria di lavoro per creare strategie per raggiungere un obiettivo,
		per non perdersi, o rifare il lavoro. Inoltre contribuisce ad inibire dare risposte ovvie, o scegliere strategie semplici che vengono in mente per prima.
	</p>
	<p>Imagination network (future mode): si attiva ogni volta che concentriamo l'attenzione su noi stessi, sui ns sogni ad occhi aperti, gli obiettivi futuri.
		Inoltre è anche il centro della compassione, dove proviamo a metterci in ascolto verso l'altro, e ad aprirci vs nuove idee</p>
	<p>Background attention network (filter mode): si attiva sottolineando le cose che sono interessanti per noi, e scartando quelle che non lo sono.
		Essenzialmente è un filtro, prima ancora della fase immaginativa e certamente prima della fase esecutiva, la ns mente inconsciamente filtra le info e le manda alle altre parti
	</p>
	<p>La ns corteccia è molto più estesa degli altri animali, e in particolare la parte pre-frontale, ci permette di simulare le possibilità degli eventi, di
		separare noi stessi dalla situazione presente e proiettarci vs un futuro.
	</p>

	<p>Impariamo molto bene dagli altri, anche grazie al linguaggio, e questo ci mette davanti a tutte le altre specie, Però dobbiamo ammetere che i computer sono più efficienti, ma ne parliamo dopo</p>
</Notes>		
</Slide>
<Slide>
	<h5>confirmation bias</h5>
	<DueTre />
	<Notes>
<p> Creatività richiede quindi grande conoscenza di quello che è successo prima e hanno fatto gli altri, e grande lungimiranza per pensare fuori dal gruppo.
	Quello che possiamo creare è una evoluzione di quello che abbiamo già assorbito
</p>
<p>Se si confronta per esempio i musicisti o gli artisti visivi di diversi nazioni, nel passato (prima di internet) 
	ci si rende conto che sono fortemente influenzati dalla cultura del paese di origine... non è che un Ravi Shankar non fosse tecnicamente in grado di comporre un pezzo di Ennio Morricone, e viceversa,
	ma semplicemente ognuno si porta dietro un bagaglio culturale e di conoscenza che è unico e specifico
</p>
<p>Il ns cervello continuamente cerca di confrontare e correlare le informazioni che gli arrivano, con quelle che già conosce: 
	il famoso "confirmation bias", ossia cerchiamo prove per confermare quello che presumiamo sia già vero. Il ns cervello si sforza di mettere i nuovi input dentro a categorie già conosciute</p>
<p>
Questo aspetto è particolarmente problematico oggi a causa dell'effetto amplificato degli algoritmi dei social network, i quali giocano proprio su questo per proporci contenuti che non ci fanno uscira dalla bolla</p>
<p>vedi terrapiattisti, scientology, religioni, la nostra mente fa di tutto per evitare le incertezze, ma l'ironia è che è proprio lì che devi andare per pensare fuori dal coro ed essere creativo</p>
<p>In sintesi si può dire che un creativo è in grado di farsi delle domande ed essere critico delle risposte</p>



		</Notes>		
	</Slide>
</Slide>		
<Slide>
	<Slide background="/3/via-lattea.png">
		<h2>Analogie apprendimento animale e artificiale</h2>
		<ul style="margin:70px;">
			<li>4 <i class="green">μm</i> (micron) il più piccolo neurone, +1000 volte più grande di un transistor di 3<i class="yellow">nm</i> </li>
			<li>Moscerino della frutta (Fruit Fly): 100 mila neuroni</li>
			<li>Scarafaggio: Un milione di neuroni</li>
			<li>Topo: 75 milioni di neuroni</li>
			<li>Gatto: Un miliardo di neuroni</li>
			<li>Scimpanzè: 7 miliardi di neuroni</li>
			<li>Elefante: 23 miliardi di neuroni</li>
			<li>Deep Learning chip: 2.6 trilioni (on 7 nm scale)</li>
		</ul>
		
		
		<Img src="/3/chip-scale5.png" height={"60vh"} class_=""/>
		<br>
		<q style="font-size: xx-large;">Abbiamo riscontrato che, in media, il cervello umano ha 86 miliardi di neuroni. E non uno dei cervelli che abbiamo esaminato finora raggiunge i 100 miliardi </q>
		<q style="font-size: xx-large;">
			Anche se può sembrare una piccola differenza la quantità di 14 miliardi di neuroni è praticamente il numero di neuroni presente in un cervello di babbuino o quasi la metà del numero di neuroni nel cervello di gorilla. Ecco, questa differenza in realtà è abbastanza grande
		</q>
		<i style="font-size: large;">Dr.ssa Suzana Herculano-Houze</i>

		<Notes>
		<p>L'unità di base per il cervello biologico è il neurone. Il loro compito
			è quello di trasmettere l'impulso elettrico dall'assone ai punti più terminali. Questo è come il ns corpo percepisce la luce, lo stimolo della pressione del tatto, il calore e via dicendo. I segnali dei neuroni specializzati vengono trasmessi dal ns sistema nervoso al cervello composto anch'esso di miliardi di neuroni intercomunicanti, creando una rete. </p>
		<p>
			Ma quanti sono? I ricercatori hanno recentemente stimato in 86 miliardi il num di neuroni, 
			che certo è minore dei 200/400 miliardi di stelle nella via Lattea ma comunque è un bel numero.
		</p>
		<p>Ma quanto sono grandi? Ci sono diversi tipi di neuroni con finzioni specializzate.
			Il più piccolo può avere un corpo cellulare di soli 4 micron di larghezza, 
			mentre i corpi cellulari dei neuroni più grandi possono avere una larghezza di 100 micron.</p>
		<p>Nel cervelletto è concentrata più della metà, quindi anche la densità non è omogenea.</p>
		<p>Ogni neurone può stabilire connessioni fino a 1.000 neuroni</p>
		<p>In una rete biologica il segnale elettrico è catturato dai dendriti. Essi combinandosi formano insieme un segnale più forte. Se il segnale è sufficientemente forte il neurone manda l'impulso attraverso l'assone verso i terminali che passa il segnale ai dendriti del neurone successivo. E' importante notare che il segnale d'entrata arriva da fonti multiple e le trasmette a sua volta a molteplici dendriti.</p>
		<p>L'unità computazionale di base per i computer sono i transistor. Più che il numero, ha senso parlare della densità raggiunta, comunque quest'anno, un processore di deep learning ha montato 2.6 trilioni di transistor in un singolo chip</p>
		<p>L'unità computazionale di base per le reti neurali, anch'esso è chiamato neurone. 
			Riceve input da qualche altro nodo o da fonti esterne e genera un output</p>
		<p></p>
	</Notes>
</Slide>		
<Slide>
	<h2>Creatività per l'AI</h2>
	<Img src="/3/analogie.png" width={"80vh"} />
	<Notes>
		<p>In un certo qual modo i meccanismi creativi dell'AI sono assimilabili a quelli umani, (non a caso visto che per decenni le scienze cognitive hanno cercato di modellare i ns meccanismi di apprendimento)</p>
		<p>Catturare parole chiave (prompt/filter) e cosa è associato ad esso (train), istruire un modello mentale (plan), e immaginare qualcosa di nuovo (future/inference)</p>
		<p>I bambini sentono tante volte la parola cane e alla fine imparano e lo associano all'animale, o meglio imparano a riconoscere le caratteristiche distintive che lo rendono cane e non un altro animale</p>
		<p>Anche gli altri animali imparano, e come per le persone, più abbondanti sono gli stimoli e maggiore sarà lo sviluppo della corteccia cerebrale, tuttavia le connessioni e le attivazioni del cervello umano sono molto più estese.</p>
		<p>Gli algoritmi di ML richiedono migliaia a volte anche milioni di immagini per un training di base, e poche decine per affinare il modello (finetuning), come per noi una volta imparata una cosa simile, basta poco per ripassarla</p>
		</Notes>
	</Slide>

	
		<Slide>
		<h2>Come vengono codificate le immagini?</h2>
		<p> Latent Space</p>
		<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/sV2FOdGqlX0?si=kFBtn7o_QRP46TK5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> -->
		<video data-autoplay controls width="80%">
			<source src="/3/VAE Latent Space Visualization.mp4" type="video/mp4" />
		</video>
		<p style="font-size: large;">
			<a href="https://youtu.be/sV2FOdGqlX0?si=olAVgMsR1GjziGZN">Video fatto da Aqeel Anwar</a> 
		</p>
		<Notes>
		<p>Se chiediamo al pubblico di descrivere a parole le caratteristiche di una immagine nessuno avrebbe problemi, ma se fossero espressi in linguaggio binario nessuno saprebbe cosa sono</p>
		<p>Viceversa il computer per codificare le caratteristiche che rendono unica questa immagine, deve tradurla in parametri (feature encoding)</p>
		<p>Ognuna di queste features, una volta estratte, sono rappresentate da un vettore in uno spazio multidimensionale (latent space), insieme alla descrizione testuale.</p>
		<p>Facendo il training di queste matrici viene così creata una associazione tra testo/(prompt), anch'esso diviso in token e vettorializzato, e immagine.</p>
		<p>In questo spazio esiste il cane, il gatto e tutte le variazioni intermedie in realtà inesistenti, il prompt ci indica dove navigare in questi punti nel Latent Space.</p>
		<p>Anche una piccola variazione nel prompt come una virgola, può proiettarci in un punto molto diverso del latent space rendendo il processo in parte aleatorio</p>
		</Notes>
	</Slide>		
	<Slide>
		<h2>Come funziona il training?</h2>
		<Img src="/4/NN.png" width={"50vw"} />
		<br>
		<Img src="/4/activation.png" height={"20vh"} />

		<Notes>
			<p>Come dicevamo nelle NN il neurone è l'unità di base. Ad ogni input è associato un peso (weight) assegnato a seconda di quanto è importante l'input.</p>
			<p>Il neurone applica una funzione di attivazione. Se il segnale/input è troppo basso il segnale viene scartato altrimenti il segnale prosegue al neurone successivo (Forward propagation)</p>
			<p>Ma come fa effettivamente ad imparare? Si confronta il risultato ottenuto in output con quello che ci si aspettava, e poi viene aggiustato il peso di ogni connessione di ogni nodo facendo il percorso inverso (Back propagation) </p>

			<p>Ogni passaggio  </p>
		</Notes>
	</Slide>		
	<Slide>
		<h2> Come si trasformano i numeri di nuovo in pixel? </h2>
		<Frag>Diffusion / Denoising</Frag>
		
		<Img src="/4/cat-steps.jpg" width={"100vw"} />
		<Img src="/4/dog-steps.jpg" width={"100vw"} />
		<Img src="/4/cat-dog-steps.jpg" width={"100vw"} />
			
			<Notes>
				<p>C'è poi l'operazione inversa, ossia trasformare questa rappresentazione matematica, di nuovo in una immagine fatta di pixel. Questo processo è chiamato Diffusion</p>
				<p>Questo processo inizia con una immagine fatta di noise, e con una serie di interazioni, i pixel virano verso una composizione che ha senso per gli noi umani</p>

			</Notes>
		</Slide>		
		<Slide>
			<h2>Transformer</h2>
			<p>2017 - Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin</p>
			<Img src="/4/Attention is all you need.png" height={"50vh"} />
		<Notes>
			<p>Il titolo e il lavoro di questo paper, scritto da un gruppo di ricercatori Google nel 2017, rimarrà per sempre nella storia del ML</p>
			<p>Fino a quel momento l'architettura delle deep neural networks - reti neurali (CNN e RNN) era basato su un meccanismo puro encoder-decoder, 
				loro hanno proposto un metodo più semplice basato sull'attenzione chiamato Trasformer</p>
			<p>Questo ha permesso di incrementare in maniera massiva la quantità di dati per il training, permettendo così di comprendere a fondo le relazioni 
				del linguaggio naturale e codificarlo in maniera efficiente, </p>
			<p>Grazie infatti a questi algoritmi, è stato possibile costruire dei grandi modelli del linguaggio (LLM) come OpenAI/ChatGPT, LLama, Falcon etc</p>	
			<p>I Trasformer applicati alla generazione di immagini, ha permesso di rendere efficiente l'operazione di apprendere da miliardi di immagini e capire DOVE prestare attenzione in una immagine
				Distinguere per esempio qual'è il soggetto da uno sfondo, e come l'insieme di questi parametri costituiscono il concetto di cane</p>
			<p>Le proprietà "con coda" e "con pelo" sono caratteristiche non sufficienti a descrivere univocamente un cane, 
				trovare il minimo insieme che le descrive, dimenticando cioè che non è essenziale, differenziando il segnale dal noise, è stato reso possibile grazie ai Trasformers.</p>	
			<p>Un altro modo di pensare ai Transformer è quello di vederli come algoritmi di compressione intelligenti</p>
		</Notes>
		</Slide>		
	</Slide>
	<Slide>	
		<h2>Criticità dei modelli di ML: </h2>

		<Slide>
		<h3>Specializzazione</h3>
		<Img src="/5/builder.png" height={"70vh"} />

		<Notes>
		<p> Tuttavia i modelli di AI/ML sono molto efficienti quando vengono istruiti per fare qualcosa di altamente specializzato, con compiti ristretti e ben definiti</p>
		<p>Se si istruisce un modello per creare i paesaggi con migliaia di immagini, diventerà bravissimo a creare i paesaggi ma fallirà miserabilmente a creare un viso. </p>
		<p>Stessa cosa dicasi per i sw  allenati a riconoscere tumori, non capiranno niente se gli si presenta una immagine di una mela</p>
		<p>Il ns vantaggio competitivo (per ora) rispetto al'AI è proprio questa capacità enorme di generalizzare</p>
		<p>Tuttavia conosciamo bene cosa porta una eccessiva specializzazione anche per le persone: magari bravissimi nel fare qualcosa ma con la mentalità ristretta per il resto</p>
		</Notes>

	</Slide>
	<Slide>
		<h3> Black box</h3>
		<Img src="/5/bbox.png" height={"70vh"} />

		<Notes>
			<p>Una volta creato il modello, è una scatola chiusa che nessuno sa come funziona, perché dà certi risultati e quanto siano attendibili.</p>
			<p>Però anche il ns cervello funziona così, pochi sanno cosa passa in testa a certa gente, e a volte ci sorprendiamo di noi stessi, e di come reagiamo di fronte a certe situazioni. </p>
			<p>Siamo abituati a credere le ns azioni e decisioni siano frutto di un ragionamento, ma cos'è il ragionamento se non la somma di tutti i bias/conoscenze passate? </p>
		</Notes>
	</Slide>
</Slide>

<Slide>
		<p class="par">
			Aldo Spizzichino 
		</p>
		<div class="container" style="margin-top: -30px;">
			<div class="box">
				<UnoUno {interval}/>
			</div>
			<div class="box">
				<UnoDue {interval}/>
			</div>
			<div class="box">
				<UnoTre {interval}/>								
			</div>
			<div class="box">
				<UnoQuatro {interval}/>
			</div>
		</div>
		<Notes>
			<p>Per chi non conoscesse Aldo questi sono alcune immagini dei suoi lavori che poterete trovare anche qui esposte</p>
			<p>Come potete notare ha uno stile difficilmente assimilabile agli altri artisti</p>
			
			<p>Introdurre i problemi di training</p>
			<p>Far notare gli aspetti compositivi dell'arte di Aldo</p>
		</Notes>
			
	</Slide>

	<Slide>
		<h2>Risultati ottenuti training </h2>
		<SDtrain {interval}/>
	</Slide>
	<Slide>
		<h2>Risultati ottenuti training 2 </h2>
	</Slide>
	<Slide>
		<h2>Control-net </h2>
	</Slide>
	<!-- <Slide backgroundIframe="https://hakim.se" backgroundInteractive> -->

	<Slide>
		<h2>Live demo </h2>
	</Slide>
	<Slide>
		<h2>Il lavoro per gli artisti del presente </h2>
		<Notes>
			<p>Parlare di come cambia il lavoro per tanti nel settore </p>
			<p>Fare l'esempio dei rendering architettonici</p>
		</Notes>
	</Slide>
	<Slide>
		<h2>Opere derivate, copyrights e scioperi </h2>
		<Notes>
		<p> Esempi di artisti che hanno discusso sull'argomento James Guney etc </p>
		<p>Stability.ai e litigation</p>
		<p>Recenti scioperi ad Holywood</p>
		<p>censorship</p>
		<p>bias to white man</p>
		</Notes>

	</Slide>
	


<!--



<p>Come si migliora la creatività?</p>
<p>Blocco creativo, comfort zone. La società moderna è molto concentrata sulla visione che gli altri hanno su noi invece che focalizzare l'attenzione sulla ricerca interiore</p>

-->










<!--




	<Slide>
		<Slide>
			<h2>Vertical Slides</h2>
			<p>Slides can be nested inside of each other.</p>
			<p>Use the <em>Space</em> key to navigate through all slides.</p>
			<br>
			<a href="#" class="navigate-down">
				<img class="r-frame" style="background: rgba(255,255,255,0.1);" width="178" height="238" data-src="https://static.slid.es/reveal/arrow.png" alt="Down arrow">
			</a>
		</Slide>
		<Slide>
			<h2>Basement Level 1</h2>
			<p>Nested slides are useful for adding additional detail underneath a high level horizontal slide.</p>
		</Slide>
		<Slide>
			<h2>Basement Level 2</h2>
			<p>That's it, time to go back up.</p>
			<br>
			<a href="#/2">
				<img class="r-frame" style="background: rgba(255,255,255,0.1); transform: rotate(180deg);" width="178" height="238" data-src="https://static.slid.es/reveal/arrow.png" alt="Up arrow">
			</a>
		</Slide>
	</Slide>

	<Slide>
		<h2>Slides</h2>
		<p>
			Not a coder? Not a problem. There's a fully-featured visual editor for authoring these, try it out at <a href="https://slides.com" target="_blank">https://slides.com</a>.
		</p>
	</Slide>

	<Slide autoAnimate>
		<h2 id="code-title">Pretty Code</h2>
		<Code id="code-animation" trim lineNumbers language="javascript">
			{@html `
import React, { useState } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  return (
	...
  );
}
			`}
		</Code>
		<p>Code syntax highlighting courtesy of <a href="https://highlightjs.org/usage/">highlight.js</a>.</p>
	</Slide>

	<Slide autoAnimate>
		<h2 id="code-title">Even Prettier Animations</h2>
		<Code id="code-animation" trim lineNumbers="|4,8-11|17|22-24" language="javascript">
			{@html `
import React, { useState } from 'react';

function Example() {
	const [count, setCount] = useState(0);

	return (
	&lt;div&gt;
		&lt;p&gt;You clicked {count} times&lt;/p&gt;
		&lt;button onClick={() =&gt; setCount(count + 1)}&gt;
		Click me
		&lt;/button&gt;
	&lt;/div&gt;
	);
}

function SecondExample() {
	const [count, setCount] = useState(0);

	return (
	&lt;div&gt;
		&lt;p&gt;You clicked {count} times&lt;/p&gt;
		&lt;button onClick={() =&gt; setCount(count + 1)}&gt;
		Click me
		&lt;/button&gt;
	&lt;/div&gt;
	);
}
			`}
		</Code>
	</Slide>

	<Slide>
		<h2>Point of View</h2>
		<p>
			Press <strong>ESC</strong> to enter the slide overview.
		</p>
		<p>
			Hold down the <strong>alt</strong> key (<strong>ctrl</strong> in Linux) and click on any element to zoom towards it using <a href="https://lab.hakim.se/zoom-js">zoom.js</a>. Click again to zoom back out.
		</p>
		<p>
			(NOTE: Use ctrl + click in Linux.)
		</p>
	</Slide>

	<Slide autoAnimate autoAnimateEasing="cubic-bezier(0.770, 0.000, 0.175, 1.000)">
		<h2>Auto-Animate</h2>
		<p>Automatically animate matching elements across slides with <a href="https://revealjs.com/auto-animate/">Auto-Animate</a>.</p>
		<div class="r-hstack justify-center">
			<div data-id="box1" style="background: #999; width: 50px; height: 50px; margin: 10px; border-radius: 5px;"></div>
			<div data-id="box2" style="background: #999; width: 50px; height: 50px; margin: 10px; border-radius: 5px;"></div>
			<div data-id="box3" style="background: #999; width: 50px; height: 50px; margin: 10px; border-radius: 5px;"></div>
		</div>
	</Slide>
	<Slide autoAnimate autoAnimateEasing="cubic-bezier(0.770, 0.000, 0.175, 1.000)">
		<div class="r-hstack justify-center">
			<div data-id="box1" data-auto-animate-delay="0" style="background: cyan; width: 150px; height: 100px; margin: 10px;"></div>
			<div data-id="box2" data-auto-animate-delay="0.1" style="background: magenta; width: 150px; height: 100px; margin: 10px;"></div>
			<div data-id="box3" data-auto-animate-delay="0.2" style="background: yellow; width: 150px; height: 100px; margin: 10px;"></div>
		</div>
		<h2 style="margin-top: 20px;">Auto-Animate</h2>
	</Slide>
	<Slide autoAnimate autoAnimateEasing="cubic-bezier(0.770, 0.000, 0.175, 1.000)">
		<div class="r-stack">
			<div data-id="box1" style="background: cyan; width: 300px; height: 300px; border-radius: 200px;"></div>
			<div data-id="box2" style="background: magenta; width: 200px; height: 200px; border-radius: 200px;"></div>
			<div data-id="box3" style="background: yellow; width: 100px; height: 100px; border-radius: 200px;"></div>
		</div>
		<h2 style="margin-top: 20px;">Auto-Animate</h2>
	</Slide>
	<Slide>
		<h2>Touch Optimized</h2>
		<p>
			Presentations look great on touch devices, like mobile phones and tablets. Simply swipe through your slides.
		</p>
	</Slide>

	<Slide>
		<p>Add the <code>r-fit-text</code> class to auto-size text</p>
		<h2 class="r-fit-text">FIT TEXT</h2>
	</Slide>

	<Slide>
		<Slide id="fragments">
			<h2>Fragments</h2>
			<p>Hit the next arrow...</p>
			<p class="fragment">... to step through ...</p>
			<p><span class="fragment">... a</span> <span class="fragment">fragmented</span> <span class="fragment">slide.</span></p>

			<aside class="notes">
				This slide has fragments which are also stepped through in the notes window.
			</aside>
		</Slide>
		<Slide>
			<h2>Fragment Styles</h2>
			<p>There's different types of fragments, like:</p>
			<p class="fragment grow">grow</p>
			<p class="fragment shrink">shrink</p>
			<p class="fragment fade-out">fade-out</p>
			<p>
				<span style="display: inline-block;" class="fragment fade-right">fade-right, </span>
				<span style="display: inline-block;" class="fragment fade-up">up, </span>
				<span style="display: inline-block;" class="fragment fade-down">down, </span>
				<span style="display: inline-block;" class="fragment fade-left">left</span>
			</p>
			<p class="fragment fade-in-then-out">fade-in-then-out</p>
			<p class="fragment fade-in-then-semi-out">fade-in-then-semi-out</p>
			<p>Highlight <span class="fragment highlight-red">red</span> <span class="fragment highlight-blue">blue</span> <span class="fragment highlight-green">green</span></p>
		</Slide>
	</Slide>

	<Slide id="transitions">
		<h2>Transition Styles</h2>
		<p>
			You can select from different transitions, like: <br>
			<a href="?transition=none#/transitions">None</a> -
			<a href="?transition=fade#/transitions">Fade</a> -
			<a href="?transition=slide#/transitions">Slide</a> -
			<a href="?transition=convex#/transitions">Convex</a> -
			<a href="?transition=concave#/transitions">Concave</a> -
			<a href="?transition=zoom#/transitions">Zoom</a>
		</p>
	</Slide>

	<Slide>
		<Slide background="#dddddd">
			<h2>Slide Backgrounds</h2>
			<p>
				Set <code>data-background="#dddddd"</code> on a slide to change the background color. All CSS color formats are supported.
			</p>
			<a href="#" class="navigate-down">
				<img class="r-frame" style="background: rgba(255,255,255,0.1);" width="178" height="238" data-src="https://static.slid.es/reveal/arrow.png" alt="Down arrow">
			</a>
		</Slide>
		<Slide background="https://static.slid.es/reveal/image-placeholder.png">
			<h2>Image Backgrounds</h2>
			<Code language="html">&lt;Slide background="image.png"&gt;</Code>
		</Slide>
		<Slide background="https://static.slid.es/reveal/image-placeholder.png" backgroundRepeat="repeat" backgroundSize="100px">
			<h2>Tiled Backgrounds</h2>
			<Code language="html">&lt;Slide background="image.png" backgroundRepeat="repeat" backgroundSize="100px"&gt;</Code>
		</Slide>
		<Slide backgroundVideo="https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.mp4" backgroundColor="#000000">
			<div style="background-color: rgba(0, 0, 0, 0.9); color: #fff; padding: 20px;">
				<h2>Video Backgrounds</h2>
				<pre><code class="hljs html" style="word-wrap: break-word;">&lt;Slide backgroundVideo="video.mp4,video.webm"&gt;</code></pre>
			</div>
		</Slide>
		<Slide background="http://i.giphy.com/90F8aUepslB84.gif">
			<h2>... and GIFs!</h2>
		</Slide>
	</Slide>

	<Slide transition="slide" background="#4d7e65" backgroundTransition="zoom">
		<h2>Background Transitions</h2>
		<p>
			Different background transitions are available via the backgroundTransition option. This one's called "zoom".
		</p>
		<Code language="javascript">{@html `Reveal.configure({ backgroundTransition: 'zoom' })`}</Code>
	</Slide>

	<Slide transition="slide" background="#b5533c" backgroundTransition="zoom">
		<h2>Background Transitions</h2>
		<p>
			You can override background transitions per-slide.
		</p>
		<pre><code class="hljs html" style="word-wrap: break-word;">&lt;Slide backgroundTransition="zoom"&gt;</code></pre>
	</Slide>

	<Slide backgroundIframe="https://hakim.se" backgroundInteractive>
		<div style="position: absolute; width: 40%; right: 0; box-shadow: 0 1px 4px rgba(0,0,0,0.5), 0 5px 25px rgba(0,0,0,0.2); background-color: rgba(0, 0, 0, 0.9); color: #fff; padding: 20px; font-size: 20px; text-align: left;">
			<h2>Iframe Backgrounds</h2>
			<p>Since reveal.js runs on the web, you can easily embed other web content. Try interacting with the page in the background.</p>
		</div>
	</Slide>

	<Slide>
		<h2>Marvelous List</h2>
		<ul>
			<li>No order here</li>
			<li>Or here</li>
			<li>Or here</li>
			<li>Or here</li>
		</ul>
	</Slide>

	<Slide>
		<h2>Fantastic Ordered List</h2>
		<ol>
			<li>One is smaller than...</li>
			<li>Two is smaller than...</li>
			<li>Three!</li>
		</ol>
	</Slide>

	<Slide>
		<h2>Tabular Tables</h2>
		<table>
			<thead>
				<tr>
					<th>Item</th>
					<th>Value</th>
					<th>Quantity</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>Apples</td>
					<td>$1</td>
					<td>7</td>
				</tr>
				<tr>
					<td>Lemonade</td>
					<td>$2</td>
					<td>18</td>
				</tr>
				<tr>
					<td>Bread</td>
					<td>$3</td>
					<td>2</td>
				</tr>
			</tbody>
		</table>
	</Slide>

	<Slide>
		<h2>Clever Quotes</h2>
		<p>
			These guys come in two forms, inline: <q cite="http://searchservervirtualization.techtarget.com/definition/Our-Favorite-Technology-Quotations">The nice thing about standards is that there are so many to choose from</q> and block:
		</p>
		<blockquote cite="http://searchservervirtualization.techtarget.com/definition/Our-Favorite-Technology-Quotations">
			&ldquo;For years there has been a theory that millions of monkeys typing at random on millions of typewriters would
			reproduce the entire works of Shakespeare. The Internet has proven this theory to be untrue.&rdquo;
		</blockquote>
	</Slide>

	<Slide>
		<h2>Intergalactic Interconnections</h2>
		<p>
			You can link between slides internally,
			<a href="#/2/3">like this</a>.
		</p>
	</Slide>

	<Slide>
		<h2>Speaker View</h2>
		<p>There's a <a href="https://revealjs.com/speaker-view/">speaker view</a>. It includes a timer, preview of the upcoming slide as well as your speaker notes.</p>
		<p>Press the <em>S</em> key to try it out.</p>
		<Notes>
			Oh hey, these are some notes. They'll be hidden in your presentation, but you can see them if you open the speaker notes window (hit 's' on your keyboard).
		</Notes>

	</Slide>

	<Slide>
		<h2>Export to PDF</h2>
		<p>Presentations can be <a href="https://revealjs.com/pdf-export/">exported to PDF</a>, here's an example:</p>
		<iframe data-src="https://www.slideshare.net/slideshow/embed_code/42840540" width="445" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:3px solid #666; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>
	</Slide>

	<Slide>
		<h2>Global State</h2>
		<p>
			Set <code>data-state="something"</code> on a slide and <code>"something"</code>
			will be added as a class to the document element when the slide is open. This lets you
			apply broader style changes, like switching the page background.
		</p>
	</Slide>

	<Slide state="customevent">
		<h2>State Events</h2>
		<p>
			Additionally custom events can be triggered on a per slide basis by binding to the <code>data-state</code> name.
		</p>
		<Code trim language="javascript" contenteditable>
			{@html `
Reveal.on( 'customevent', function() {
console.log( '"customevent" has fired' );
} );
			`}
		</Code>
	</Slide>

	<Slide>
		<h2>Take a Moment</h2>
		<p>
			Press B or . on your keyboard to pause the presentation. This is helpful when you're on stage and want to take distracting slides off the screen.
		</p>
	</Slide>

	<Slide>
		<h2>Much more</h2>
		<ul>
			<li>Right-to-left support</li>
			<li><a href="https://revealjs.com/api/">Extensive JavaScript API</a></li>
			<li><a href="https://revealjs.com/auto-slide/">Auto-progression</a></li>
			<li><a href="https://revealjs.com/backgrounds/#parallax-background">Parallax backgrounds</a></li>
			<li><a href="https://revealjs.com/keyboard/">Custom keyboard bindings</a></li>
		</ul>
	</Slide>

	<Slide>
		<h1>THE END</h1>
		<p>
			- <a href="https://slides.com">Try the online editor</a> <br>
			- <a href="https://github.com/hakimel/reveal.js">Source code &amp; documentation</a>
		</p>
	</Slide>
-->