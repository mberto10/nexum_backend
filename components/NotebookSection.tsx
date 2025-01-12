const fetchFromAPI = async (command: string, type: string, entryId: string) => {
  const baseUrl = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000' 
    : `https://${window.location.hostname.replace('.','-')}-3000.${window.location.hostname.split('.')[1]}.repl.co`;
  const response = await fetch(`${baseUrl}/api/command`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ command, type, entryId }),
  });

  if (!response.ok) {
    const message = `HTTP error! status: ${response.status}`;
    throw new Error(message);
  }

  const data = await response.json();
  return data;
};