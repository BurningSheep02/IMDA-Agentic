var TurndownService = require('turndown')
var turndownService = new TurndownService()

function html_to_markdown(html) {
    return turndownService.turndown(html)
}

module.exports = {
    html_to_markdown
  }


/*
    if (process.argv[2]) {
        //var html = await fetch(process.argv[2]);
        html = process.argv[2];
        //console.log(html)
        console.log('\n Loading html... \n');
        var markdown = turndownService.turndown(html);
        console.log(markdown)
        console.log('\n Completed \n')
    } else {
        console.log('No html provided');
    }
*/

