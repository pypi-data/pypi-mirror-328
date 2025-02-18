import pytest
import asyncio
import multiprocessing as mp
from unittest.mock import patch, MagicMock, AsyncMock
from spade.agent import Agent
from spade.mixins import StandaloneMixin

@pytest.mark.asyncio
async def test_start_creates_process(agent_with_behaviour):
    with patch.object(mp, 'Process') as mock_process:
        process_instance = MagicMock()
        mock_process.return_value = process_instance
        
        await agent_with_behaviour.start()
        
        mock_process.assert_called_once()
        assert mock_process.call_args[1]["args"][0] == agent_with_behaviour.__class__
        process_instance.start.assert_called_once()

@pytest.mark.asyncio
async def test_start_in_child_process(agent_with_behaviour):
    agent_with_behaviour._process = MagicMock()
    agent_with_behaviour._process.pid = 1234
    
    with patch('multiprocessing.current_process') as mock_current_process:
        mock_current_process.return_value.pid = 1234
        with patch.object(Agent, 'start') as mock_start:
            await agent_with_behaviour.start()
            mock_start.assert_called_once_with(auto_register=True)

@pytest.mark.asyncio
async def test_start_handles_error(agent_with_behaviour):
    error = AttributeError("Can't pickle local object 'agent_with_behaviour.<locals>.TestBehaviour'")
    
    with patch.object(mp, 'Process') as mock_process:
        process_instance = MagicMock()
        mock_process.return_value = process_instance
        
        def put_error(*args):
            agent_with_behaviour._start_error.put(error)
        process_instance.start.side_effect = put_error
        
        with pytest.raises(AttributeError) as exc_info:
            await agent_with_behaviour.start()
        
        assert str(exc_info.value) == str(error)
        process_instance.terminate.assert_called_once()

@pytest.mark.asyncio
async def test_stop_in_parent_process(agent_with_behaviour):
    mock_process = MagicMock()
    agent_with_behaviour._process = mock_process
    
    with patch('os.getpid') as mock_getpid:
        mock_getpid.return_value = 5678  # Different from process.pid
        mock_process.pid = 1234
        
        await agent_with_behaviour.stop()
        
        mock_process.terminate.assert_called_once()
        mock_process.join.assert_called_once_with(timeout=5)

@pytest.mark.asyncio
async def test_stop_in_child_process(agent_with_behaviour):
    mock_process = MagicMock()
    agent_with_behaviour._process = mock_process
    
    with patch('os.getpid') as mock_getpid:
        mock_getpid.return_value = 1234  # Same as process.pid
        mock_process.pid = 1234
        with patch.object(Agent, 'stop') as mock_stop:
            await agent_with_behaviour.stop()
            mock_stop.assert_called_once()

@pytest.mark.asyncio
async def test_stop_kills_if_terminate_fails(agent_with_behaviour):
    mock_process = MagicMock()
    agent_with_behaviour._process = mock_process
    mock_process.is_alive.return_value = True
    
    with patch('os.getpid') as mock_getpid:
        mock_getpid.return_value = 5678
        mock_process.pid = 1234
        
        await agent_with_behaviour.stop()
        
        mock_process.terminate.assert_called_once()
        mock_process.kill.assert_called_once()
