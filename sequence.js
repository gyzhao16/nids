function main(params) {

    let step = params.$step || 0
    delete params.$step

    var content = { "packet": params.__ow_body }
    
    switch (step) {
    	// case 0: return content
        case 0: return { action: 'nids', params: content, state: { $step: 1 } }
        // case 1: return { action: 'nids', params, state: { $step: 2 } }
        case 1: return { params }
    }
}