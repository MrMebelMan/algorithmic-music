// Configure OSC port to receive messages to (optional)
msg.setPort(57101);

foxdot = {}

msg.on('/s_new', (args) => {
	// 'hydra' is a special FoxDot synthdef that does not produce any sounds,
	// but has handy attributes that are named after Hydra functions, like "kaleid", "rotate" etc.
	// The synthdef's source code is here: https://github.com/MrMebelMan/FoxDot/blob/killa_features/FoxDot/osc/scsyndef/hydra.scd
	// Inspired by CrashServer's "video" synthdef <3

	if (args[0] === 'hydra') {
		// We don't need first 6 parameters, so we'll skip them
		args = args.slice(6);

		// Iterate over the OSC bundle and fill the "foxdot" object with synthdef's properties
		for(var i = 0; i < args.length; i += 2) {
			foxdot[args[i]] = args[i + 1]
		}
	}
});

// We want properties to update automatically, so we need to use an arrow function.
shape(() => foxdot.sample).out()

