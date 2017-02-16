
(function() {

// current chat (last created)
var smartsuppChat = parent.smartsupp.chats[smartchatId]; // global chat id
// async workaround
var smartsuppLoadInterval = setInterval(function() {
	if (!window.miwo) return; // wait until libs are loaded async
	clearInterval(smartsuppLoadInterval);
	miwo.ready(function() {
		// add internal google analytics
		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

		// setup
		miwo.cookie.document = parent.document;
		miwo.baseUrl = smartsuppChat.getOption('baseUrl');
		miwo.staticUrl = smartsuppChat.getOption('staticUrl');

		// dashboard data
		var data = {"package":"free","lang":"en","orientation":"right","hideBanner":true,"hideWidget":false,"hideOfflineBanner":true,"enableRating":true,"requireLogin":false,"hideOfflineChat":true,"muteSounds":true,"isEnabledEvents":false,"banner":{"type":"arrow","options":{}},"translates":{"online":{"title":"Purethemes Support"},"offline":{},"widget":{"online":"Chat with our developer"},"banner":{"arrow":{},"bubble":{}}},"colors":{"primary":"#01ADFF","banner":"#494949","widget":"#01ADFF","primaryText":"#FFFFFF"},"theme":{"name":"flat","options":{"widgetRadius":"0"}},"api":{"basic":true,"banner":true,"events":false,"groups":false,"theme":true}};
		data.baseLang = 'en';
		data.browserLang = 'en';
		data.avatar = '/chats/89736/avatar-ynpzpsc82l.png';
		data.host = 's11.smartsupp.com';		data.packageName = 'free';
		data.logoUrl = '';
		data.logoSrc = '';
		data.logoSmSrc = '';
		data.smartlook = window.smartlook;

		// create configurator
		var configurator = new Miwo.Configurator();
		configurator.addConfig(App.DefaultConfig.getConfig());
		configurator.addConfig(App.ClientConfig.getConfig(data));
		configurator.addConfig(App.ChatConfig.getConfig(smartsuppChat));

		// create and run app
		configurator.ext(new Chat.ChatExtension());
		var container = configurator.createContainer();
		container.get('miwo.application').run();
	});
}, 50);

// smartlook module start
// smartlook module end

})();

