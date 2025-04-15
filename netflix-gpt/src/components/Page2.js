import React, { useEffect, useState } from 'react';
import STLViewer from '../StlLoader/STLViewer';
import { useSelector, useDispatch } from 'react-redux';
import { addMessage } from './Store/Slices/Messages';
import { v4 as uuidv4 } from 'uuid';

const Page2 = () => {
  const { messages } = useSelector((state) => state.messages);
  const dispatch = useDispatch();
  const [modelUrl, setModelUrl] = useState('/box.stl');

  useEffect(() => {
    if (messages.length === 0) return;

    const lastMessage = messages[messages.length - 1];
    console.log("api call with",lastMessage);
    if (lastMessage.role !== 'user') {
      console.log("we have issues to dfix");
      return;
    }
      
    

    const fetchSTL = async () => {
      try {
        const response = await fetch("http://localhost:8000/3dobj", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ query: lastMessage.content })
        });

        if (!response.ok) throw new Error("Failed to fetch STL");

        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        setModelUrl(url);

        dispatch(addMessage({
          id: uuidv4(),
          role: 'system',
          content: 'Image generated successfully'
        }));
      } catch (error) {
        console.error("Error fetching STL:", error);
        dispatch(addMessage({
          id: uuidv4(),
          role: 'system',
          content: 'Try again — some error occurred'
        }));
      }
    };

    fetchSTL();
  }, [messages, dispatch]);

  return (
    <div className="h-screen w-screen flex flex-col items-center justify-center bg-[#030013] md:w-[40%]">
      <div className="flex justify-end text-white font-bold text-lg p-4">BOARD</div>
      <div className="flex justify-center w-full h-full">
        <STLViewer fileUrl={modelUrl} />
      </div>
    </div>
  );
};

export default Page2;
