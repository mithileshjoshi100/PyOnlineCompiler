console.log("script called")
const textarea = document.querySelector('.code')
const lineNumbers = document.querySelector('.line-numbers')

textarea.addEventListener('keyup', event => {
    console.log('changes')
const numberOfLines = event.target.value.split('\n').length
console.log(numberOfLines)
lineNumbers.innerHTML = Array(numberOfLines)
     .fill('<span></span>')
     .join('')
})

textarea.addEventListener('keydown', event => {
if (event.key === 'Tab') {
    const start = textarea.selectionStart
    const end = textarea.selectionEnd
    textarea.value = textarea.value.substring(0, start) + '    ' + textarea.value.substring(end)
    event.preventDefault()
}
})