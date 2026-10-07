import { useState, useEffect } from "react";
import SelectSmall from "../components/CommonDropDown";
import { TextField, Button, Typography } from "@mui/material";

export const PromptPage = () => {
  const [models, setModels] = useState<string[]>([]);
  const [selectedModel, setSelectedModel] = useState<string>("");
  const [input, setInput] = useState<string>("");
  const [messages, setMessages] = useState<Array<{ role: string; content: string }>>([]);

  useEffect(() => {
    fetch("http://localhost:8000/models")
      .then((res) => res.json())
      .then((data) => {
        setModels(data.models || []);
        if (data.models?.length > 0) setSelectedModel(data.models[0]);
      });
  }, []);

  const handleSend = async () => {
    if (!input.trim() || !selectedModel) return;

    const userMsg = { role: "user", content: input };
    const updatedMessages = [...messages, userMsg];
    setMessages([...updatedMessages, { role: "assistant", content: "" }]);
    setInput("");

    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ model: selectedModel, messages: updatedMessages }),
    });

    const reader = response.body?.getReader();
    const decoder = new TextDecoder();
    let assistantReply = "";

    while (reader) {
      const { done, value } = await reader.read();
      if (done) break;
      assistantReply += decoder.decode(value);
      setMessages([...updatedMessages, { role: "assistant", content: assistantReply }]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <Typography variant="h6">Local AI Assistant</Typography>
        <SelectSmall options={models} value={selectedModel} onChange={setSelectedModel} />
      </div>

      <div className="messages-area">
        {messages.map((msg, i) => (
          <div key={i} className={`message-bubble ${msg.role}`}>
            {msg.content}
          </div>
        ))}
      </div>

      <div className="input-bar">
        <TextField
          fullWidth
          size="small"
          placeholder="Ask something..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
        />
        <Button variant="contained" onClick={handleSend}>Send</Button>
      </div>
    </div>
  );
};
