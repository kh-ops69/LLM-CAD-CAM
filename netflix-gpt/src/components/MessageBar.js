import React from 'react'

function MessageBar({ sentence }) {
  const isUser = sentence.role === 'user';

  return (
    <div
      className={`max-w-[80%] p-3 px-6 rounded-2xl ${
        isUser ? 'bg-[#8b9199] self-end' : 'bg-[#414040] self-start'
      } text-white`}
    >
      {sentence.content}
    </div>
  );
}

export default MessageBar
