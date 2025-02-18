import sys
import traceback
from os.path import abspath, dirname, join, basename
from socket import error
from hashlib import md5
from datetime import datetime
from gevent.pywsgi import WSGIHandler, WSGIServer

from web3socket.policyserver import FlashPolicyServer
from web3socket import Web3Socket

import gevent
assert gevent.version_info >= (0, 13, 2), 'Newer version of gevent is required to run web3socket.server'

__all__ = ['Web3socketHandler', 'Web3socketServer']


class Web3socketHandler(WSGIHandler):

    def run_application(self):
        path = self.environ.get('PATH_INFO')
        content_type = self.server.data_handlers.get(path)
        if content_type is not None:
            self.serve_file(basename(path), content_type)
            return

        web3socket_mode = False

        if Web3Socket.is_socket(self.environ):
            self.status = 'web3socket'
            self.log_request()
            self.environ['web3socket'] = Web3Socket(self.environ, self.socket, self.rfile)
            web3socket_mode = True
        try:
            self.result = self.application(self.environ, self.start_response)
            if self.result is not None:
                self.process_result()
        except:
            web3socket = self.environ.get('web3socket')
            if web3socket is not None:
                web3socket.close()
            raise
        finally:
            if web3socket_mode:
                # we own the socket now, make sure pywsgi does not try to read from it:
                self.socket = None

    def serve_file(self, filename, content_type):
        from web3socket import data
        path = join(dirname(abspath(data.__file__)), filename)
        if self.server.etags.get(path) == (self.environ.get('HTTP_IF_NONE_MATCH') or 'x'):
            self.start_response('304 Not Modifed', [])
            self.write('')
            return
        try:
            body = open(path).read()
        except IOError, ex:
            sys.stderr.write('Cannot open %s: %s\n' % (path, ex))
            self.start_response('404 Not Found', [])
            self.write('')
            return
        etag = md5(body).hexdigest()
        self.server.etags[path] = etag
        self.start_response('200 OK', [('Content-Type', content_type),
                                       ('Content-Length', str(len(body))),
                                       ('Etag', etag)])
        self.write(body)


class Web3socketServer(WSGIServer):

    handler_class = Web3socketHandler
    data_handlers = {
        '/web3socket/Web3SocketMain.swf': 'application/x-shockwave-flash',
        '/web3socket/flashsocket.js': 'text/javascript'
    }
    etags = {}

    def __init__(self, listener, application=None, policy_server=True, backlog=None,
                 spawn='default', log='default', handler_class=None, environ=None, **ssl_args):
        if policy_server is True:
            self.policy_server = FlashPolicyServer()
        elif isinstance(policy_server, tuple):
            self.policy_server = FlashPolicyServer(policy_server)
        elif policy_server:
            raise TypeError('Expected tuple or boolean: %r' % (policy_server, ))
        else:
            self.policy_server = None
        super(Web3socketServer, self).__init__(listener, application, backlog=backlog, spawn=spawn, log=log,
                                              handler_class=handler_class, environ=environ, **ssl_args)

    def start_accepting(self):
        self._start_policy_server()
        super(Web3socketServer, self).start_accepting()
        self.log_message('%s accepting connections on %s', self.__class__.__name__, _format_address(self))

    def _start_policy_server(self):
        server = self.policy_server
        if server is not None:
            try:
                server.start()
                self.log_message('%s accepting connections on %s', server.__class__.__name__, _format_address(server))
            except error, ex:
                sys.stderr.write('FAILED to start %s on %s: %s\n' % (server.__class__.__name__, _format_address(server), ex))
            except Exception:
                traceback.print_exc()
                sys.stderr.write('FAILED to start %s on %s\n' % (server.__class__.__name__, _format_address(server)))

    def kill(self):
        if self.policy_server is not None:
            self.policy_server.kill()
        super(Web3socketServer, self).kill()

    def log_message(self, message, *args):
        log = self.log
        if log is not None:
            try:
                message = message % args
            except Exception:
                traceback.print_exc()
                try:
                    message = '%r %r' % (message, args)
                except Exception:
                    traceback.print_exc()
            log.write('%s %s\n' % (datetime.now().replace(microsecond=0), message))


def _format_address(server):
    try:
        if server.server_host == '0.0.0.0':
            return ':%s' % server.server_port
        return '%s:%s' % (server.server_host, server.server_port)
    except Exception:
        traceback.print_exc()
