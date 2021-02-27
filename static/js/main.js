var addnote = document.getElementById('add-note')
var completebtn = document.getElementsByClassName('complete')

addnote.addEventListener('click', function(event){
    event.preventDefault()
    document.getElementById('note-container').classList.add('d-none')
    document.getElementById('note-form').classList.remove('d-none')
    document.getElementById('add-note').classList.add('d-none')
})


 for (var i = 0; i < completebtn.length; i++){
     completebtn[i].addEventListener('click', function(e){
         e.preventDefault()
         var noteId = this.dataset.note
         var action = this.dataset.action
         console.log('noteId:', noteId, 'action:', action)
         completeUncomplete(noteId,action)
         
     })
 }
 function completeUncomplete(noteId, action){
     var url = '/complete/'
     fetch(url, {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json',
         },
         body:JSON.stringify({'noteId':noteId, 'action': action})
     })
     .then((response)=>{
         return response.json()
     })
     .then((data)=>{
         console.log('data:', data)
         location.reload()
     })
 }
