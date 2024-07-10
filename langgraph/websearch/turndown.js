var TurndownService = require('turndown')
var turndownService = new TurndownService()

function html_to_markdown(html) {
    return turndownService.turndown(html)
}

module.exports = {
    html_to_markdown
  }


