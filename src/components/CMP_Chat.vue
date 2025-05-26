<template>
  <div class="chat">
    <ul>
      <li v-for="msg in messages" :key="msg.id">{{ msg.text }}</li>
    </ul>
    <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Введите сообщение..." />    
  </div>
</template>

<script>
export default {

  data() {
    return {
      newMessage: "",
      messages: [],
      broadcastMessages: []
    };
  },
  
  mounted() {
    // Подпишемся на события через socket.io
    this.$socket.on('chat_message', (data) => {
      this.messages.push({ id: Date.now() + Math.random(), text: data });
    });
  },

  methods: {
    sendMessage() {
      if (this.newMessage.trim()) {
        this.$socket.emit('chat_message', this.newMessage);
        this.newMessage = "";
      }
    }
  }
  
};
</script>
