r'''
# Amazon MQ for ActiveMQ XML configuration v5.15.16 bindings

<!--BEGIN STABILITY BANNER-->---


| Features                   | Stability                                                                                    |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| All types are experimental | ![Experimental](https://img.shields.io/badge/experimental-important.svg?style=for-the-badge) |

> **Experimental:** All types in this module are experimental and are under active development. They are subject to non-backward compatible
> changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes
> will be announced in the release notes. This means that while you may use them, you may need to update your source code when upgrading to a
> newer version of this package.

---
<!--END STABILITY BANNER-->

This package provides strongly-typed configuration bindings for Amazon MQ for ActiveMQ version 5.15.16. It enables you to define your ActiveMQ broker configurations in code instead of raw XML.

The types in this library are intended to be used with the [@cdklabs/cdk-amazonmq](https://github.com/cdklabs/cdk-amazonmq) library and allow for providing strongly-typed configuration of ActiveMQ brokers that is generated from [the XML schema definition tailored for the Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html#working-with-spring-xml-configuration-files).

An example of using this library can be found below:

```python
// Basic broker configuration
const broker = new Broker({
  schedulePeriodForDestinationPurge: 10000,
  start: false
}, {
  // Destination interceptors configuration
  destinationInterceptors: [
    // ... interceptor configuration
  ],

  // Persistence configuration
  persistenceAdapter: new KahaDB({
    // ... persistence configuration
  }),

  // Policy configuration
  destinationPolicy: new PolicyMap({
    // ... policy configuration
  }),

  // ... other sections
});
```

> **LDAP Integration Note:**
> Amazon MQ for ActiveMQ [enables LDAP integration](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-authentication-authorization.html) which requires using `cachedLDAPAuthorizationMap`. See [ActiveMQ documentation](https://activemq.apache.org/components/classic/documentation/cached-ldap-authorization-module) for more details. The types in this package include the `CachedLDAPAuthorizationMap` type with attributes specifically enabled by Amazon MQ for ActiveMQ.
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AbortSlowAckConsumerStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "abort_connection": "abortConnection",
        "check_period": "checkPeriod",
        "ignore_idle_consumers": "ignoreIdleConsumers",
        "ignore_network_consumers": "ignoreNetworkConsumers",
        "max_slow_count": "maxSlowCount",
        "max_slow_duration": "maxSlowDuration",
        "max_time_since_last_ack": "maxTimeSinceLastAck",
        "name": "name",
    },
)
class AbortSlowAckConsumerStrategyAttributes:
    def __init__(
        self,
        *,
        abort_connection: typing.Optional[builtins.bool] = None,
        check_period: typing.Optional[jsii.Number] = None,
        ignore_idle_consumers: typing.Optional[builtins.bool] = None,
        ignore_network_consumers: typing.Optional[builtins.bool] = None,
        max_slow_count: typing.Optional[jsii.Number] = None,
        max_slow_duration: typing.Optional[jsii.Number] = None,
        max_time_since_last_ack: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param abort_connection: 
        :param check_period: 
        :param ignore_idle_consumers: 
        :param ignore_network_consumers: 
        :param max_slow_count: 
        :param max_slow_duration: 
        :param max_time_since_last_ack: 
        :param name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__816d4e5bfd7583265c3326c7f9bdb14b5d2d4159647e3d0a64977d7ccdfb539d)
            check_type(argname="argument abort_connection", value=abort_connection, expected_type=type_hints["abort_connection"])
            check_type(argname="argument check_period", value=check_period, expected_type=type_hints["check_period"])
            check_type(argname="argument ignore_idle_consumers", value=ignore_idle_consumers, expected_type=type_hints["ignore_idle_consumers"])
            check_type(argname="argument ignore_network_consumers", value=ignore_network_consumers, expected_type=type_hints["ignore_network_consumers"])
            check_type(argname="argument max_slow_count", value=max_slow_count, expected_type=type_hints["max_slow_count"])
            check_type(argname="argument max_slow_duration", value=max_slow_duration, expected_type=type_hints["max_slow_duration"])
            check_type(argname="argument max_time_since_last_ack", value=max_time_since_last_ack, expected_type=type_hints["max_time_since_last_ack"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if abort_connection is not None:
            self._values["abort_connection"] = abort_connection
        if check_period is not None:
            self._values["check_period"] = check_period
        if ignore_idle_consumers is not None:
            self._values["ignore_idle_consumers"] = ignore_idle_consumers
        if ignore_network_consumers is not None:
            self._values["ignore_network_consumers"] = ignore_network_consumers
        if max_slow_count is not None:
            self._values["max_slow_count"] = max_slow_count
        if max_slow_duration is not None:
            self._values["max_slow_duration"] = max_slow_duration
        if max_time_since_last_ack is not None:
            self._values["max_time_since_last_ack"] = max_time_since_last_ack
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def abort_connection(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("abort_connection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def check_period(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("check_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_idle_consumers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ignore_idle_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ignore_network_consumers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ignore_network_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_slow_count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_slow_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_slow_duration(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_slow_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_time_since_last_ack(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_time_since_last_ack")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AbortSlowAckConsumerStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AbortSlowConsumerStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "abort_connection": "abortConnection",
        "check_period": "checkPeriod",
        "ignore_network_consumers": "ignoreNetworkConsumers",
        "max_slow_count": "maxSlowCount",
        "max_slow_duration": "maxSlowDuration",
        "name": "name",
    },
)
class AbortSlowConsumerStrategyAttributes:
    def __init__(
        self,
        *,
        abort_connection: typing.Optional[builtins.bool] = None,
        check_period: typing.Optional[jsii.Number] = None,
        ignore_network_consumers: typing.Optional[builtins.bool] = None,
        max_slow_count: typing.Optional[jsii.Number] = None,
        max_slow_duration: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param abort_connection: 
        :param check_period: 
        :param ignore_network_consumers: 
        :param max_slow_count: 
        :param max_slow_duration: 
        :param name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3438312b1f8861fc2732067c2c1df4c88231f936acddfe106d4b78678151839b)
            check_type(argname="argument abort_connection", value=abort_connection, expected_type=type_hints["abort_connection"])
            check_type(argname="argument check_period", value=check_period, expected_type=type_hints["check_period"])
            check_type(argname="argument ignore_network_consumers", value=ignore_network_consumers, expected_type=type_hints["ignore_network_consumers"])
            check_type(argname="argument max_slow_count", value=max_slow_count, expected_type=type_hints["max_slow_count"])
            check_type(argname="argument max_slow_duration", value=max_slow_duration, expected_type=type_hints["max_slow_duration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if abort_connection is not None:
            self._values["abort_connection"] = abort_connection
        if check_period is not None:
            self._values["check_period"] = check_period
        if ignore_network_consumers is not None:
            self._values["ignore_network_consumers"] = ignore_network_consumers
        if max_slow_count is not None:
            self._values["max_slow_count"] = max_slow_count
        if max_slow_duration is not None:
            self._values["max_slow_duration"] = max_slow_duration
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def abort_connection(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("abort_connection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def check_period(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("check_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_network_consumers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ignore_network_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_slow_count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_slow_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_slow_duration(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_slow_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AbortSlowConsumerStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AuthorizationEntryAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "admin": "admin",
        "queue": "queue",
        "read": "read",
        "temp_queue": "tempQueue",
        "temp_topic": "tempTopic",
        "topic": "topic",
        "write": "write",
    },
)
class AuthorizationEntryAttributes:
    def __init__(
        self,
        *,
        admin: typing.Optional[builtins.str] = None,
        queue: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        temp_queue: typing.Optional[builtins.bool] = None,
        temp_topic: typing.Optional[builtins.bool] = None,
        topic: typing.Optional[builtins.str] = None,
        write: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin: 
        :param queue: 
        :param read: 
        :param temp_queue: 
        :param temp_topic: 
        :param topic: 
        :param write: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca913e11cc9f95a989edf8dc13ff6a8ccd2fea12cd97661b7dabb0fcd52f4e95)
            check_type(argname="argument admin", value=admin, expected_type=type_hints["admin"])
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument temp_queue", value=temp_queue, expected_type=type_hints["temp_queue"])
            check_type(argname="argument temp_topic", value=temp_topic, expected_type=type_hints["temp_topic"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument write", value=write, expected_type=type_hints["write"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if admin is not None:
            self._values["admin"] = admin
        if queue is not None:
            self._values["queue"] = queue
        if read is not None:
            self._values["read"] = read
        if temp_queue is not None:
            self._values["temp_queue"] = temp_queue
        if temp_topic is not None:
            self._values["temp_topic"] = temp_topic
        if topic is not None:
            self._values["topic"] = topic
        if write is not None:
            self._values["write"] = write

    @builtins.property
    def admin(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("admin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queue(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def temp_queue(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_queue")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def temp_topic(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_topic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("write")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationEntryAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AuthorizationMapElements",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_entries": "authorizationEntries",
        "default_entry": "defaultEntry",
        "temp_destination_authorization_entry": "tempDestinationAuthorizationEntry",
    },
)
class AuthorizationMapElements:
    def __init__(
        self,
        *,
        authorization_entries: typing.Optional[typing.Sequence["IAuthorizationMapAuthorizationEntry"]] = None,
        default_entry: typing.Optional["IAuthorizationMapDefaultEntry"] = None,
        temp_destination_authorization_entry: typing.Optional["TempDestinationAuthorizationEntry"] = None,
    ) -> None:
        '''
        :param authorization_entries: 
        :param default_entry: 
        :param temp_destination_authorization_entry: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ea8d070ea58412c08a3c6c3ee54b6e5f44482e0862e9aae8b4ded60bc0963a1)
            check_type(argname="argument authorization_entries", value=authorization_entries, expected_type=type_hints["authorization_entries"])
            check_type(argname="argument default_entry", value=default_entry, expected_type=type_hints["default_entry"])
            check_type(argname="argument temp_destination_authorization_entry", value=temp_destination_authorization_entry, expected_type=type_hints["temp_destination_authorization_entry"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authorization_entries is not None:
            self._values["authorization_entries"] = authorization_entries
        if default_entry is not None:
            self._values["default_entry"] = default_entry
        if temp_destination_authorization_entry is not None:
            self._values["temp_destination_authorization_entry"] = temp_destination_authorization_entry

    @builtins.property
    def authorization_entries(
        self,
    ) -> typing.Optional[typing.List["IAuthorizationMapAuthorizationEntry"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("authorization_entries")
        return typing.cast(typing.Optional[typing.List["IAuthorizationMapAuthorizationEntry"]], result)

    @builtins.property
    def default_entry(self) -> typing.Optional["IAuthorizationMapDefaultEntry"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("default_entry")
        return typing.cast(typing.Optional["IAuthorizationMapDefaultEntry"], result)

    @builtins.property
    def temp_destination_authorization_entry(
        self,
    ) -> typing.Optional["TempDestinationAuthorizationEntry"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_destination_authorization_entry")
        return typing.cast(typing.Optional["TempDestinationAuthorizationEntry"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationMapElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AuthorizationPluginElements",
    jsii_struct_bases=[],
    name_mapping={"authorization_map": "authorizationMap"},
)
class AuthorizationPluginElements:
    def __init__(
        self,
        *,
        authorization_map: typing.Optional["IAuthorizationPluginMap"] = None,
    ) -> None:
        '''
        :param authorization_map: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36be44b87e5caee82a19a320bc7247a9d0420edb55e86d554041ac7c9a40f0c5)
            check_type(argname="argument authorization_map", value=authorization_map, expected_type=type_hints["authorization_map"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authorization_map is not None:
            self._values["authorization_map"] = authorization_map

    @builtins.property
    def authorization_map(self) -> typing.Optional["IAuthorizationPluginMap"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("authorization_map")
        return typing.cast(typing.Optional["IAuthorizationPluginMap"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPluginElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.BrokerAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "advisory_support": "advisorySupport",
        "allow_temp_auto_creation_on_send": "allowTempAutoCreationOnSend",
        "anonymous_producer_advisory_support": "anonymousProducerAdvisorySupport",
        "cache_temp_destinations": "cacheTempDestinations",
        "consumer_system_usage_portion": "consumerSystemUsagePortion",
        "dedicated_task_runner": "dedicatedTaskRunner",
        "delete_all_messages_on_startup": "deleteAllMessagesOnStartup",
        "keep_durable_subs_active": "keepDurableSubsActive",
        "max_purged_destinations_per_sweep": "maxPurgedDestinationsPerSweep",
        "monitor_connection_splits": "monitorConnectionSplits",
        "offline_durable_subscriber_task_schedule": "offlineDurableSubscriberTaskSchedule",
        "offline_durable_subscriber_timeout": "offlineDurableSubscriberTimeout",
        "persistence_thread_priority": "persistenceThreadPriority",
        "persistent": "persistent",
        "populate_jmsx_user_id": "populateJMSXUserID",
        "producer_system_usage_portion": "producerSystemUsagePortion",
        "reject_durable_consumers": "rejectDurableConsumers",
        "rollback_only_on_async_exception": "rollbackOnlyOnAsyncException",
        "schedule_period_for_destination_purge": "schedulePeriodForDestinationPurge",
        "scheduler_support": "schedulerSupport",
        "split_system_usage_for_producers_consumers": "splitSystemUsageForProducersConsumers",
        "start": "start",
        "system_usage": "systemUsage",
        "task_runner_priority": "taskRunnerPriority",
        "time_before_purge_temp_destinations": "timeBeforePurgeTempDestinations",
        "use_authenticated_principal_for_jmsx_user_id": "useAuthenticatedPrincipalForJMSXUserID",
        "use_mirrored_queues": "useMirroredQueues",
        "use_temp_mirrored_queues": "useTempMirroredQueues",
        "use_virtual_dest_subs": "useVirtualDestSubs",
        "use_virtual_dest_subs_on_creation": "useVirtualDestSubsOnCreation",
        "use_virtual_topics": "useVirtualTopics",
    },
)
class BrokerAttributes:
    def __init__(
        self,
        *,
        advisory_support: typing.Optional[builtins.str] = None,
        allow_temp_auto_creation_on_send: typing.Optional[builtins.bool] = None,
        anonymous_producer_advisory_support: typing.Optional[builtins.bool] = None,
        cache_temp_destinations: typing.Optional[builtins.bool] = None,
        consumer_system_usage_portion: typing.Optional[jsii.Number] = None,
        dedicated_task_runner: typing.Optional[builtins.bool] = None,
        delete_all_messages_on_startup: typing.Optional[builtins.str] = None,
        keep_durable_subs_active: typing.Optional[builtins.bool] = None,
        max_purged_destinations_per_sweep: typing.Optional[jsii.Number] = None,
        monitor_connection_splits: typing.Optional[builtins.bool] = None,
        offline_durable_subscriber_task_schedule: typing.Optional[jsii.Number] = None,
        offline_durable_subscriber_timeout: typing.Optional[jsii.Number] = None,
        persistence_thread_priority: typing.Optional[jsii.Number] = None,
        persistent: typing.Optional[builtins.str] = None,
        populate_jmsx_user_id: typing.Optional[builtins.bool] = None,
        producer_system_usage_portion: typing.Optional[jsii.Number] = None,
        reject_durable_consumers: typing.Optional[builtins.bool] = None,
        rollback_only_on_async_exception: typing.Optional[builtins.bool] = None,
        schedule_period_for_destination_purge: typing.Optional[jsii.Number] = None,
        scheduler_support: typing.Optional[builtins.str] = None,
        split_system_usage_for_producers_consumers: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.bool] = None,
        system_usage: typing.Optional[builtins.str] = None,
        task_runner_priority: typing.Optional[jsii.Number] = None,
        time_before_purge_temp_destinations: typing.Optional[jsii.Number] = None,
        use_authenticated_principal_for_jmsx_user_id: typing.Optional[builtins.bool] = None,
        use_mirrored_queues: typing.Optional[builtins.bool] = None,
        use_temp_mirrored_queues: typing.Optional[builtins.bool] = None,
        use_virtual_dest_subs: typing.Optional[builtins.bool] = None,
        use_virtual_dest_subs_on_creation: typing.Optional[builtins.bool] = None,
        use_virtual_topics: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param advisory_support: 
        :param allow_temp_auto_creation_on_send: 
        :param anonymous_producer_advisory_support: 
        :param cache_temp_destinations: 
        :param consumer_system_usage_portion: 
        :param dedicated_task_runner: 
        :param delete_all_messages_on_startup: 
        :param keep_durable_subs_active: 
        :param max_purged_destinations_per_sweep: 
        :param monitor_connection_splits: 
        :param offline_durable_subscriber_task_schedule: 
        :param offline_durable_subscriber_timeout: 
        :param persistence_thread_priority: 
        :param persistent: 
        :param populate_jmsx_user_id: 
        :param producer_system_usage_portion: 
        :param reject_durable_consumers: 
        :param rollback_only_on_async_exception: 
        :param schedule_period_for_destination_purge: 
        :param scheduler_support: 
        :param split_system_usage_for_producers_consumers: 
        :param start: 
        :param system_usage: 
        :param task_runner_priority: 
        :param time_before_purge_temp_destinations: 
        :param use_authenticated_principal_for_jmsx_user_id: 
        :param use_mirrored_queues: 
        :param use_temp_mirrored_queues: 
        :param use_virtual_dest_subs: 
        :param use_virtual_dest_subs_on_creation: 
        :param use_virtual_topics: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33236241482e941c1050a0a4182e06a7e8c310b6b3c03d31f08168915c49c5e4)
            check_type(argname="argument advisory_support", value=advisory_support, expected_type=type_hints["advisory_support"])
            check_type(argname="argument allow_temp_auto_creation_on_send", value=allow_temp_auto_creation_on_send, expected_type=type_hints["allow_temp_auto_creation_on_send"])
            check_type(argname="argument anonymous_producer_advisory_support", value=anonymous_producer_advisory_support, expected_type=type_hints["anonymous_producer_advisory_support"])
            check_type(argname="argument cache_temp_destinations", value=cache_temp_destinations, expected_type=type_hints["cache_temp_destinations"])
            check_type(argname="argument consumer_system_usage_portion", value=consumer_system_usage_portion, expected_type=type_hints["consumer_system_usage_portion"])
            check_type(argname="argument dedicated_task_runner", value=dedicated_task_runner, expected_type=type_hints["dedicated_task_runner"])
            check_type(argname="argument delete_all_messages_on_startup", value=delete_all_messages_on_startup, expected_type=type_hints["delete_all_messages_on_startup"])
            check_type(argname="argument keep_durable_subs_active", value=keep_durable_subs_active, expected_type=type_hints["keep_durable_subs_active"])
            check_type(argname="argument max_purged_destinations_per_sweep", value=max_purged_destinations_per_sweep, expected_type=type_hints["max_purged_destinations_per_sweep"])
            check_type(argname="argument monitor_connection_splits", value=monitor_connection_splits, expected_type=type_hints["monitor_connection_splits"])
            check_type(argname="argument offline_durable_subscriber_task_schedule", value=offline_durable_subscriber_task_schedule, expected_type=type_hints["offline_durable_subscriber_task_schedule"])
            check_type(argname="argument offline_durable_subscriber_timeout", value=offline_durable_subscriber_timeout, expected_type=type_hints["offline_durable_subscriber_timeout"])
            check_type(argname="argument persistence_thread_priority", value=persistence_thread_priority, expected_type=type_hints["persistence_thread_priority"])
            check_type(argname="argument persistent", value=persistent, expected_type=type_hints["persistent"])
            check_type(argname="argument populate_jmsx_user_id", value=populate_jmsx_user_id, expected_type=type_hints["populate_jmsx_user_id"])
            check_type(argname="argument producer_system_usage_portion", value=producer_system_usage_portion, expected_type=type_hints["producer_system_usage_portion"])
            check_type(argname="argument reject_durable_consumers", value=reject_durable_consumers, expected_type=type_hints["reject_durable_consumers"])
            check_type(argname="argument rollback_only_on_async_exception", value=rollback_only_on_async_exception, expected_type=type_hints["rollback_only_on_async_exception"])
            check_type(argname="argument schedule_period_for_destination_purge", value=schedule_period_for_destination_purge, expected_type=type_hints["schedule_period_for_destination_purge"])
            check_type(argname="argument scheduler_support", value=scheduler_support, expected_type=type_hints["scheduler_support"])
            check_type(argname="argument split_system_usage_for_producers_consumers", value=split_system_usage_for_producers_consumers, expected_type=type_hints["split_system_usage_for_producers_consumers"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument system_usage", value=system_usage, expected_type=type_hints["system_usage"])
            check_type(argname="argument task_runner_priority", value=task_runner_priority, expected_type=type_hints["task_runner_priority"])
            check_type(argname="argument time_before_purge_temp_destinations", value=time_before_purge_temp_destinations, expected_type=type_hints["time_before_purge_temp_destinations"])
            check_type(argname="argument use_authenticated_principal_for_jmsx_user_id", value=use_authenticated_principal_for_jmsx_user_id, expected_type=type_hints["use_authenticated_principal_for_jmsx_user_id"])
            check_type(argname="argument use_mirrored_queues", value=use_mirrored_queues, expected_type=type_hints["use_mirrored_queues"])
            check_type(argname="argument use_temp_mirrored_queues", value=use_temp_mirrored_queues, expected_type=type_hints["use_temp_mirrored_queues"])
            check_type(argname="argument use_virtual_dest_subs", value=use_virtual_dest_subs, expected_type=type_hints["use_virtual_dest_subs"])
            check_type(argname="argument use_virtual_dest_subs_on_creation", value=use_virtual_dest_subs_on_creation, expected_type=type_hints["use_virtual_dest_subs_on_creation"])
            check_type(argname="argument use_virtual_topics", value=use_virtual_topics, expected_type=type_hints["use_virtual_topics"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if advisory_support is not None:
            self._values["advisory_support"] = advisory_support
        if allow_temp_auto_creation_on_send is not None:
            self._values["allow_temp_auto_creation_on_send"] = allow_temp_auto_creation_on_send
        if anonymous_producer_advisory_support is not None:
            self._values["anonymous_producer_advisory_support"] = anonymous_producer_advisory_support
        if cache_temp_destinations is not None:
            self._values["cache_temp_destinations"] = cache_temp_destinations
        if consumer_system_usage_portion is not None:
            self._values["consumer_system_usage_portion"] = consumer_system_usage_portion
        if dedicated_task_runner is not None:
            self._values["dedicated_task_runner"] = dedicated_task_runner
        if delete_all_messages_on_startup is not None:
            self._values["delete_all_messages_on_startup"] = delete_all_messages_on_startup
        if keep_durable_subs_active is not None:
            self._values["keep_durable_subs_active"] = keep_durable_subs_active
        if max_purged_destinations_per_sweep is not None:
            self._values["max_purged_destinations_per_sweep"] = max_purged_destinations_per_sweep
        if monitor_connection_splits is not None:
            self._values["monitor_connection_splits"] = monitor_connection_splits
        if offline_durable_subscriber_task_schedule is not None:
            self._values["offline_durable_subscriber_task_schedule"] = offline_durable_subscriber_task_schedule
        if offline_durable_subscriber_timeout is not None:
            self._values["offline_durable_subscriber_timeout"] = offline_durable_subscriber_timeout
        if persistence_thread_priority is not None:
            self._values["persistence_thread_priority"] = persistence_thread_priority
        if persistent is not None:
            self._values["persistent"] = persistent
        if populate_jmsx_user_id is not None:
            self._values["populate_jmsx_user_id"] = populate_jmsx_user_id
        if producer_system_usage_portion is not None:
            self._values["producer_system_usage_portion"] = producer_system_usage_portion
        if reject_durable_consumers is not None:
            self._values["reject_durable_consumers"] = reject_durable_consumers
        if rollback_only_on_async_exception is not None:
            self._values["rollback_only_on_async_exception"] = rollback_only_on_async_exception
        if schedule_period_for_destination_purge is not None:
            self._values["schedule_period_for_destination_purge"] = schedule_period_for_destination_purge
        if scheduler_support is not None:
            self._values["scheduler_support"] = scheduler_support
        if split_system_usage_for_producers_consumers is not None:
            self._values["split_system_usage_for_producers_consumers"] = split_system_usage_for_producers_consumers
        if start is not None:
            self._values["start"] = start
        if system_usage is not None:
            self._values["system_usage"] = system_usage
        if task_runner_priority is not None:
            self._values["task_runner_priority"] = task_runner_priority
        if time_before_purge_temp_destinations is not None:
            self._values["time_before_purge_temp_destinations"] = time_before_purge_temp_destinations
        if use_authenticated_principal_for_jmsx_user_id is not None:
            self._values["use_authenticated_principal_for_jmsx_user_id"] = use_authenticated_principal_for_jmsx_user_id
        if use_mirrored_queues is not None:
            self._values["use_mirrored_queues"] = use_mirrored_queues
        if use_temp_mirrored_queues is not None:
            self._values["use_temp_mirrored_queues"] = use_temp_mirrored_queues
        if use_virtual_dest_subs is not None:
            self._values["use_virtual_dest_subs"] = use_virtual_dest_subs
        if use_virtual_dest_subs_on_creation is not None:
            self._values["use_virtual_dest_subs_on_creation"] = use_virtual_dest_subs_on_creation
        if use_virtual_topics is not None:
            self._values["use_virtual_topics"] = use_virtual_topics

    @builtins.property
    def advisory_support(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_support")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allow_temp_auto_creation_on_send(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("allow_temp_auto_creation_on_send")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def anonymous_producer_advisory_support(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("anonymous_producer_advisory_support")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cache_temp_destinations(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cache_temp_destinations")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def consumer_system_usage_portion(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("consumer_system_usage_portion")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dedicated_task_runner(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dedicated_task_runner")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def delete_all_messages_on_startup(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("delete_all_messages_on_startup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keep_durable_subs_active(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("keep_durable_subs_active")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_purged_destinations_per_sweep(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_purged_destinations_per_sweep")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitor_connection_splits(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("monitor_connection_splits")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def offline_durable_subscriber_task_schedule(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("offline_durable_subscriber_task_schedule")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def offline_durable_subscriber_timeout(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("offline_durable_subscriber_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def persistence_thread_priority(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("persistence_thread_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def persistent(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("persistent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def populate_jmsx_user_id(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("populate_jmsx_user_id")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def producer_system_usage_portion(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("producer_system_usage_portion")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def reject_durable_consumers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("reject_durable_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def rollback_only_on_async_exception(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("rollback_only_on_async_exception")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def schedule_period_for_destination_purge(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("schedule_period_for_destination_purge")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheduler_support(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("scheduler_support")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def split_system_usage_for_producers_consumers(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("split_system_usage_for_producers_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def start(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def system_usage(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("system_usage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_runner_priority(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("task_runner_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def time_before_purge_temp_destinations(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("time_before_purge_temp_destinations")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_authenticated_principal_for_jmsx_user_id(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_authenticated_principal_for_jmsx_user_id")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_mirrored_queues(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_mirrored_queues")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_temp_mirrored_queues(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_temp_mirrored_queues")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_virtual_dest_subs(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_virtual_dest_subs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_virtual_dest_subs_on_creation(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_virtual_dest_subs_on_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_virtual_topics(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_virtual_topics")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BrokerAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.BrokerElements",
    jsii_struct_bases=[],
    name_mapping={
        "destination_interceptors": "destinationInterceptors",
        "destination_policy": "destinationPolicy",
        "destinations": "destinations",
        "network_connectors": "networkConnectors",
        "persistence_adapter": "persistenceAdapter",
        "plugins": "plugins",
        "system_usage": "systemUsage",
        "transport_connectors": "transportConnectors",
    },
)
class BrokerElements:
    def __init__(
        self,
        *,
        destination_interceptors: typing.Optional[typing.Sequence["IBrokerDestinationInterceptor"]] = None,
        destination_policy: typing.Optional["PolicyMap"] = None,
        destinations: typing.Optional[typing.Sequence["IBrokerDestination"]] = None,
        network_connectors: typing.Optional[typing.Sequence["NetworkConnector"]] = None,
        persistence_adapter: typing.Optional["KahaDB"] = None,
        plugins: typing.Optional[typing.Sequence["IBrokerPlugin"]] = None,
        system_usage: typing.Optional["SystemUsage"] = None,
        transport_connectors: typing.Optional[typing.Sequence["TransportConnector"]] = None,
    ) -> None:
        '''
        :param destination_interceptors: 
        :param destination_policy: 
        :param destinations: 
        :param network_connectors: 
        :param persistence_adapter: 
        :param plugins: 
        :param system_usage: 
        :param transport_connectors: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__417062601f86bee8c4fd23717a3ff86a1fc7e55b6c213b42c4de5cecffed428f)
            check_type(argname="argument destination_interceptors", value=destination_interceptors, expected_type=type_hints["destination_interceptors"])
            check_type(argname="argument destination_policy", value=destination_policy, expected_type=type_hints["destination_policy"])
            check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            check_type(argname="argument network_connectors", value=network_connectors, expected_type=type_hints["network_connectors"])
            check_type(argname="argument persistence_adapter", value=persistence_adapter, expected_type=type_hints["persistence_adapter"])
            check_type(argname="argument plugins", value=plugins, expected_type=type_hints["plugins"])
            check_type(argname="argument system_usage", value=system_usage, expected_type=type_hints["system_usage"])
            check_type(argname="argument transport_connectors", value=transport_connectors, expected_type=type_hints["transport_connectors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination_interceptors is not None:
            self._values["destination_interceptors"] = destination_interceptors
        if destination_policy is not None:
            self._values["destination_policy"] = destination_policy
        if destinations is not None:
            self._values["destinations"] = destinations
        if network_connectors is not None:
            self._values["network_connectors"] = network_connectors
        if persistence_adapter is not None:
            self._values["persistence_adapter"] = persistence_adapter
        if plugins is not None:
            self._values["plugins"] = plugins
        if system_usage is not None:
            self._values["system_usage"] = system_usage
        if transport_connectors is not None:
            self._values["transport_connectors"] = transport_connectors

    @builtins.property
    def destination_interceptors(
        self,
    ) -> typing.Optional[typing.List["IBrokerDestinationInterceptor"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("destination_interceptors")
        return typing.cast(typing.Optional[typing.List["IBrokerDestinationInterceptor"]], result)

    @builtins.property
    def destination_policy(self) -> typing.Optional["PolicyMap"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("destination_policy")
        return typing.cast(typing.Optional["PolicyMap"], result)

    @builtins.property
    def destinations(self) -> typing.Optional[typing.List["IBrokerDestination"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("destinations")
        return typing.cast(typing.Optional[typing.List["IBrokerDestination"]], result)

    @builtins.property
    def network_connectors(self) -> typing.Optional[typing.List["NetworkConnector"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("network_connectors")
        return typing.cast(typing.Optional[typing.List["NetworkConnector"]], result)

    @builtins.property
    def persistence_adapter(self) -> typing.Optional["KahaDB"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("persistence_adapter")
        return typing.cast(typing.Optional["KahaDB"], result)

    @builtins.property
    def plugins(self) -> typing.Optional[typing.List["IBrokerPlugin"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("plugins")
        return typing.cast(typing.Optional[typing.List["IBrokerPlugin"]], result)

    @builtins.property
    def system_usage(self) -> typing.Optional["SystemUsage"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("system_usage")
        return typing.cast(typing.Optional["SystemUsage"], result)

    @builtins.property
    def transport_connectors(
        self,
    ) -> typing.Optional[typing.List["TransportConnector"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("transport_connectors")
        return typing.cast(typing.Optional[typing.List["TransportConnector"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BrokerElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CachedLDAPAuthorizationMapAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "legacy_group_mapping": "legacyGroupMapping",
        "queue_search_base": "queueSearchBase",
        "refresh_interval": "refreshInterval",
        "temp_search_base": "tempSearchBase",
        "topic_search_base": "topicSearchBase",
    },
)
class CachedLDAPAuthorizationMapAttributes:
    def __init__(
        self,
        *,
        legacy_group_mapping: typing.Optional[builtins.bool] = None,
        queue_search_base: typing.Optional[builtins.str] = None,
        refresh_interval: typing.Optional[jsii.Number] = None,
        temp_search_base: typing.Optional[builtins.str] = None,
        topic_search_base: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param legacy_group_mapping: 
        :param queue_search_base: 
        :param refresh_interval: 
        :param temp_search_base: 
        :param topic_search_base: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__484fed5b2043e609169f4d2eddf970d9a21c5f322351007bdbe1fffecd9321bd)
            check_type(argname="argument legacy_group_mapping", value=legacy_group_mapping, expected_type=type_hints["legacy_group_mapping"])
            check_type(argname="argument queue_search_base", value=queue_search_base, expected_type=type_hints["queue_search_base"])
            check_type(argname="argument refresh_interval", value=refresh_interval, expected_type=type_hints["refresh_interval"])
            check_type(argname="argument temp_search_base", value=temp_search_base, expected_type=type_hints["temp_search_base"])
            check_type(argname="argument topic_search_base", value=topic_search_base, expected_type=type_hints["topic_search_base"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if legacy_group_mapping is not None:
            self._values["legacy_group_mapping"] = legacy_group_mapping
        if queue_search_base is not None:
            self._values["queue_search_base"] = queue_search_base
        if refresh_interval is not None:
            self._values["refresh_interval"] = refresh_interval
        if temp_search_base is not None:
            self._values["temp_search_base"] = temp_search_base
        if topic_search_base is not None:
            self._values["topic_search_base"] = topic_search_base

    @builtins.property
    def legacy_group_mapping(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("legacy_group_mapping")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def queue_search_base(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue_search_base")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def refresh_interval(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("refresh_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def temp_search_base(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_search_base")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_search_base(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic_search_base")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CachedLDAPAuthorizationMapAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CachedMessageGroupMapFactoryAttributes",
    jsii_struct_bases=[],
    name_mapping={"cache_size": "cacheSize"},
)
class CachedMessageGroupMapFactoryAttributes:
    def __init__(self, *, cache_size: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param cache_size: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c021fe2103540ddf6c5824eabf75d06071687aeb44fbc93a30f04a98bf9d7aca)
            check_type(argname="argument cache_size", value=cache_size, expected_type=type_hints["cache_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cache_size is not None:
            self._values["cache_size"] = cache_size

    @builtins.property
    def cache_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cache_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CachedMessageGroupMapFactoryAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ClientIdFilterDispatchPolicyAttributes",
    jsii_struct_bases=[],
    name_mapping={"ptp_client_id": "ptpClientId", "ptp_suffix": "ptpSuffix"},
)
class ClientIdFilterDispatchPolicyAttributes:
    def __init__(
        self,
        *,
        ptp_client_id: typing.Optional[builtins.str] = None,
        ptp_suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ptp_client_id: 
        :param ptp_suffix: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55f192922949bc3410849c08dce90ef485834345e1972e51db7861cc2fbdf0ef)
            check_type(argname="argument ptp_client_id", value=ptp_client_id, expected_type=type_hints["ptp_client_id"])
            check_type(argname="argument ptp_suffix", value=ptp_suffix, expected_type=type_hints["ptp_suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ptp_client_id is not None:
            self._values["ptp_client_id"] = ptp_client_id
        if ptp_suffix is not None:
            self._values["ptp_suffix"] = ptp_suffix

    @builtins.property
    def ptp_client_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ptp_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ptp_suffix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ptp_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClientIdFilterDispatchPolicyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CompositeQueueAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "concurrent_send": "concurrentSend",
        "copy_message": "copyMessage",
        "forward_only": "forwardOnly",
        "name": "name",
    },
)
class CompositeQueueAttributes:
    def __init__(
        self,
        *,
        concurrent_send: typing.Optional[builtins.bool] = None,
        copy_message: typing.Optional[builtins.bool] = None,
        forward_only: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param concurrent_send: 
        :param copy_message: 
        :param forward_only: 
        :param name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fea3a5eeeaebdf98b5f3858133ffc5af14ef44ab178d4ea29e326d7758188ca1)
            check_type(argname="argument concurrent_send", value=concurrent_send, expected_type=type_hints["concurrent_send"])
            check_type(argname="argument copy_message", value=copy_message, expected_type=type_hints["copy_message"])
            check_type(argname="argument forward_only", value=forward_only, expected_type=type_hints["forward_only"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if concurrent_send is not None:
            self._values["concurrent_send"] = concurrent_send
        if copy_message is not None:
            self._values["copy_message"] = copy_message
        if forward_only is not None:
            self._values["forward_only"] = forward_only
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def concurrent_send(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("concurrent_send")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def copy_message(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("copy_message")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def forward_only(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("forward_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompositeQueueAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CompositeQueueElements",
    jsii_struct_bases=[],
    name_mapping={"forward_to": "forwardTo"},
)
class CompositeQueueElements:
    def __init__(
        self,
        *,
        forward_to: typing.Optional[typing.Sequence["ICompositeQueueForwardTo"]] = None,
    ) -> None:
        '''
        :param forward_to: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8cc069ee6c0e313fa768f631fb2ba39058f4bdc9b21f957d92bca5c6dd50c70)
            check_type(argname="argument forward_to", value=forward_to, expected_type=type_hints["forward_to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if forward_to is not None:
            self._values["forward_to"] = forward_to

    @builtins.property
    def forward_to(self) -> typing.Optional[typing.List["ICompositeQueueForwardTo"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("forward_to")
        return typing.cast(typing.Optional[typing.List["ICompositeQueueForwardTo"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompositeQueueElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CompositeTopicAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "concurrent_send": "concurrentSend",
        "copy_message": "copyMessage",
        "forward_only": "forwardOnly",
        "name": "name",
    },
)
class CompositeTopicAttributes:
    def __init__(
        self,
        *,
        concurrent_send: typing.Optional[builtins.bool] = None,
        copy_message: typing.Optional[builtins.bool] = None,
        forward_only: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param concurrent_send: 
        :param copy_message: 
        :param forward_only: 
        :param name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39ee33e76b38c2d63ef5e12e7ab3c0802408439741c9b8a321a1cbc95829fc4f)
            check_type(argname="argument concurrent_send", value=concurrent_send, expected_type=type_hints["concurrent_send"])
            check_type(argname="argument copy_message", value=copy_message, expected_type=type_hints["copy_message"])
            check_type(argname="argument forward_only", value=forward_only, expected_type=type_hints["forward_only"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if concurrent_send is not None:
            self._values["concurrent_send"] = concurrent_send
        if copy_message is not None:
            self._values["copy_message"] = copy_message
        if forward_only is not None:
            self._values["forward_only"] = forward_only
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def concurrent_send(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("concurrent_send")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def copy_message(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("copy_message")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def forward_only(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("forward_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompositeTopicAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CompositeTopicElements",
    jsii_struct_bases=[],
    name_mapping={"forward_to": "forwardTo"},
)
class CompositeTopicElements:
    def __init__(
        self,
        *,
        forward_to: typing.Optional[typing.Sequence["ICompositeTopicForwardTo"]] = None,
    ) -> None:
        '''
        :param forward_to: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a86f745d8984e09be513b38c446cd680a0cc985dd78ca34dda7c22dc9d1a01e)
            check_type(argname="argument forward_to", value=forward_to, expected_type=type_hints["forward_to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if forward_to is not None:
            self._values["forward_to"] = forward_to

    @builtins.property
    def forward_to(self) -> typing.Optional[typing.List["ICompositeTopicForwardTo"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("forward_to")
        return typing.cast(typing.Optional[typing.List["ICompositeTopicForwardTo"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompositeTopicElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ConditionalNetworkBridgeFilterFactoryAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "rate_duration": "rateDuration",
        "rate_limit": "rateLimit",
        "replay_delay": "replayDelay",
        "replay_when_no_consumers": "replayWhenNoConsumers",
    },
)
class ConditionalNetworkBridgeFilterFactoryAttributes:
    def __init__(
        self,
        *,
        rate_duration: typing.Optional[jsii.Number] = None,
        rate_limit: typing.Optional[jsii.Number] = None,
        replay_delay: typing.Optional[jsii.Number] = None,
        replay_when_no_consumers: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param rate_duration: 
        :param rate_limit: 
        :param replay_delay: 
        :param replay_when_no_consumers: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6513d9e9ea3daa5e567f8a8394b3bdac49855004f4e18422af302cf8c2f826)
            check_type(argname="argument rate_duration", value=rate_duration, expected_type=type_hints["rate_duration"])
            check_type(argname="argument rate_limit", value=rate_limit, expected_type=type_hints["rate_limit"])
            check_type(argname="argument replay_delay", value=replay_delay, expected_type=type_hints["replay_delay"])
            check_type(argname="argument replay_when_no_consumers", value=replay_when_no_consumers, expected_type=type_hints["replay_when_no_consumers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if rate_duration is not None:
            self._values["rate_duration"] = rate_duration
        if rate_limit is not None:
            self._values["rate_limit"] = rate_limit
        if replay_delay is not None:
            self._values["replay_delay"] = replay_delay
        if replay_when_no_consumers is not None:
            self._values["replay_when_no_consumers"] = replay_when_no_consumers

    @builtins.property
    def rate_duration(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("rate_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rate_limit(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("rate_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replay_delay(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("replay_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replay_when_no_consumers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("replay_when_no_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConditionalNetworkBridgeFilterFactoryAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ConstantPendingMessageLimitStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={"limit": "limit"},
)
class ConstantPendingMessageLimitStrategyAttributes:
    def __init__(self, *, limit: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param limit: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc6fff10dc8874486da7c565aa124d27a595cbcd48fa6e84c155d110f8ac8a3f)
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if limit is not None:
            self._values["limit"] = limit

    @builtins.property
    def limit(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConstantPendingMessageLimitStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.DiscardingAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "enable_audit": "enableAudit",
        "expiration": "expiration",
        "max_audit_depth": "maxAuditDepth",
        "max_producers_to_audit": "maxProducersToAudit",
        "process_expired": "processExpired",
        "process_non_persistent": "processNonPersistent",
    },
)
class DiscardingAttributes:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[builtins.str] = None,
        enable_audit: typing.Optional[builtins.bool] = None,
        expiration: typing.Optional[jsii.Number] = None,
        max_audit_depth: typing.Optional[jsii.Number] = None,
        max_producers_to_audit: typing.Optional[jsii.Number] = None,
        process_expired: typing.Optional[builtins.bool] = None,
        process_non_persistent: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param dead_letter_queue: 
        :param enable_audit: 
        :param expiration: 
        :param max_audit_depth: 
        :param max_producers_to_audit: 
        :param process_expired: 
        :param process_non_persistent: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2cbd128c8c9c8c2a065b7fc59d7dd95f6f731ee12bb144058cdf95553d33365)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument enable_audit", value=enable_audit, expected_type=type_hints["enable_audit"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument max_audit_depth", value=max_audit_depth, expected_type=type_hints["max_audit_depth"])
            check_type(argname="argument max_producers_to_audit", value=max_producers_to_audit, expected_type=type_hints["max_producers_to_audit"])
            check_type(argname="argument process_expired", value=process_expired, expected_type=type_hints["process_expired"])
            check_type(argname="argument process_non_persistent", value=process_non_persistent, expected_type=type_hints["process_non_persistent"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if enable_audit is not None:
            self._values["enable_audit"] = enable_audit
        if expiration is not None:
            self._values["expiration"] = expiration
        if max_audit_depth is not None:
            self._values["max_audit_depth"] = max_audit_depth
        if max_producers_to_audit is not None:
            self._values["max_producers_to_audit"] = max_producers_to_audit
        if process_expired is not None:
            self._values["process_expired"] = process_expired
        if process_non_persistent is not None:
            self._values["process_non_persistent"] = process_non_persistent

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_audit(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("enable_audit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def expiration(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_audit_depth(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_audit_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_producers_to_audit(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_producers_to_audit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def process_expired(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("process_expired")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def process_non_persistent(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("process_non_persistent")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiscardingAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.DiscardingDLQBrokerPluginAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "drop_all": "dropAll",
        "drop_only": "dropOnly",
        "drop_temporary_queues": "dropTemporaryQueues",
        "drop_temporary_topics": "dropTemporaryTopics",
        "report_interval": "reportInterval",
    },
)
class DiscardingDLQBrokerPluginAttributes:
    def __init__(
        self,
        *,
        drop_all: typing.Optional[builtins.bool] = None,
        drop_only: typing.Optional[builtins.str] = None,
        drop_temporary_queues: typing.Optional[builtins.bool] = None,
        drop_temporary_topics: typing.Optional[builtins.bool] = None,
        report_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param drop_all: 
        :param drop_only: 
        :param drop_temporary_queues: 
        :param drop_temporary_topics: 
        :param report_interval: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3d10da1babb28c5d2891fc6ec89b793eb63fbd35fc3e68dae569219b835c658)
            check_type(argname="argument drop_all", value=drop_all, expected_type=type_hints["drop_all"])
            check_type(argname="argument drop_only", value=drop_only, expected_type=type_hints["drop_only"])
            check_type(argname="argument drop_temporary_queues", value=drop_temporary_queues, expected_type=type_hints["drop_temporary_queues"])
            check_type(argname="argument drop_temporary_topics", value=drop_temporary_topics, expected_type=type_hints["drop_temporary_topics"])
            check_type(argname="argument report_interval", value=report_interval, expected_type=type_hints["report_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if drop_all is not None:
            self._values["drop_all"] = drop_all
        if drop_only is not None:
            self._values["drop_only"] = drop_only
        if drop_temporary_queues is not None:
            self._values["drop_temporary_queues"] = drop_temporary_queues
        if drop_temporary_topics is not None:
            self._values["drop_temporary_topics"] = drop_temporary_topics
        if report_interval is not None:
            self._values["report_interval"] = report_interval

    @builtins.property
    def drop_all(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("drop_all")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def drop_only(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("drop_only")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def drop_temporary_queues(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("drop_temporary_queues")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def drop_temporary_topics(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("drop_temporary_topics")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def report_interval(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("report_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiscardingDLQBrokerPluginAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FilteredDestinationAttributes",
    jsii_struct_bases=[],
    name_mapping={"queue": "queue", "selector": "selector", "topic": "topic"},
)
class FilteredDestinationAttributes:
    def __init__(
        self,
        *,
        queue: typing.Optional[builtins.str] = None,
        selector: typing.Optional[builtins.str] = None,
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param queue: 
        :param selector: 
        :param topic: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50fa0228dec4d45f18f78f29cee3a8505f39f80e7aa031d8efeec64233a74aa5)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if queue is not None:
            self._values["queue"] = queue
        if selector is not None:
            self._values["selector"] = selector
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def queue(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selector(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FilteredDestinationAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FixedCountSubscriptionRecoveryPolicyAttributes",
    jsii_struct_bases=[],
    name_mapping={"maximum_size": "maximumSize"},
)
class FixedCountSubscriptionRecoveryPolicyAttributes:
    def __init__(self, *, maximum_size: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param maximum_size: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7adb44d41d8e49fcbb46ef92514c621a67cb332f291d6c9ae4a09310e948996e)
            check_type(argname="argument maximum_size", value=maximum_size, expected_type=type_hints["maximum_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if maximum_size is not None:
            self._values["maximum_size"] = maximum_size

    @builtins.property
    def maximum_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("maximum_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FixedCountSubscriptionRecoveryPolicyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FixedSizedSubscriptionRecoveryPolicyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_size": "maximumSize",
        "use_shared_buffer": "useSharedBuffer",
    },
)
class FixedSizedSubscriptionRecoveryPolicyAttributes:
    def __init__(
        self,
        *,
        maximum_size: typing.Optional[jsii.Number] = None,
        use_shared_buffer: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param maximum_size: 
        :param use_shared_buffer: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79a9b5917136dc09decbf89720beebac050e6eeb81ea26144d2cc51b9252209d)
            check_type(argname="argument maximum_size", value=maximum_size, expected_type=type_hints["maximum_size"])
            check_type(argname="argument use_shared_buffer", value=use_shared_buffer, expected_type=type_hints["use_shared_buffer"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if maximum_size is not None:
            self._values["maximum_size"] = maximum_size
        if use_shared_buffer is not None:
            self._values["use_shared_buffer"] = use_shared_buffer

    @builtins.property
    def maximum_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("maximum_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_shared_buffer(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_shared_buffer")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FixedSizedSubscriptionRecoveryPolicyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ForcePersistencyModeBrokerPluginAttributes",
    jsii_struct_bases=[],
    name_mapping={"persistence_flag": "persistenceFlag"},
)
class ForcePersistencyModeBrokerPluginAttributes:
    def __init__(
        self,
        *,
        persistence_flag: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param persistence_flag: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__738246b0909f76598acb4b4b2b6a1297c150d6820aad0e923260d22e59c430d9)
            check_type(argname="argument persistence_flag", value=persistence_flag, expected_type=type_hints["persistence_flag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if persistence_flag is not None:
            self._values["persistence_flag"] = persistence_flag

    @builtins.property
    def persistence_flag(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("persistence_flag")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ForcePersistencyModeBrokerPluginAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IAuthorizationMapAuthorizationEntry"
)
class IAuthorizationMapAuthorizationEntry(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IAuthorizationMapAuthorizationEntryProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IAuthorizationMapAuthorizationEntry"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAuthorizationMapAuthorizationEntry).__jsii_proxy_class__ = lambda : _IAuthorizationMapAuthorizationEntryProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IAuthorizationMapDefaultEntry"
)
class IAuthorizationMapDefaultEntry(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IAuthorizationMapDefaultEntryProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IAuthorizationMapDefaultEntry"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAuthorizationMapDefaultEntry).__jsii_proxy_class__ = lambda : _IAuthorizationMapDefaultEntryProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IAuthorizationPluginMap"
)
class IAuthorizationPluginMap(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IAuthorizationPluginMapProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IAuthorizationPluginMap"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAuthorizationPluginMap).__jsii_proxy_class__ = lambda : _IAuthorizationPluginMapProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IBrokerDestination"
)
class IBrokerDestination(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IBrokerDestinationProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IBrokerDestination"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBrokerDestination).__jsii_proxy_class__ = lambda : _IBrokerDestinationProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IBrokerDestinationInterceptor"
)
class IBrokerDestinationInterceptor(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IBrokerDestinationInterceptorProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IBrokerDestinationInterceptor"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBrokerDestinationInterceptor).__jsii_proxy_class__ = lambda : _IBrokerDestinationInterceptorProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IBrokerPlugin"
)
class IBrokerPlugin(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IBrokerPluginProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IBrokerPlugin"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBrokerPlugin).__jsii_proxy_class__ = lambda : _IBrokerPluginProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ICompositeQueueForwardTo"
)
class ICompositeQueueForwardTo(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _ICompositeQueueForwardToProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ICompositeQueueForwardTo"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICompositeQueueForwardTo).__jsii_proxy_class__ = lambda : _ICompositeQueueForwardToProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ICompositeTopicForwardTo"
)
class ICompositeTopicForwardTo(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _ICompositeTopicForwardToProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ICompositeTopicForwardTo"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICompositeTopicForwardTo).__jsii_proxy_class__ = lambda : _ICompositeTopicForwardToProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.INetworkConnectorDurableDestination"
)
class INetworkConnectorDurableDestination(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _INetworkConnectorDurableDestinationProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.INetworkConnectorDurableDestination"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkConnectorDurableDestination).__jsii_proxy_class__ = lambda : _INetworkConnectorDurableDestinationProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.INetworkConnectorDynamicallyIncludedDestination"
)
class INetworkConnectorDynamicallyIncludedDestination(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _INetworkConnectorDynamicallyIncludedDestinationProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.INetworkConnectorDynamicallyIncludedDestination"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkConnectorDynamicallyIncludedDestination).__jsii_proxy_class__ = lambda : _INetworkConnectorDynamicallyIncludedDestinationProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.INetworkConnectorExcludedDestination"
)
class INetworkConnectorExcludedDestination(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _INetworkConnectorExcludedDestinationProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.INetworkConnectorExcludedDestination"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkConnectorExcludedDestination).__jsii_proxy_class__ = lambda : _INetworkConnectorExcludedDestinationProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.INetworkConnectorStaticallyIncludedDestination"
)
class INetworkConnectorStaticallyIncludedDestination(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _INetworkConnectorStaticallyIncludedDestinationProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.INetworkConnectorStaticallyIncludedDestination"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkConnectorStaticallyIncludedDestination).__jsii_proxy_class__ = lambda : _INetworkConnectorStaticallyIncludedDestinationProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryDeadLetterStrategy"
)
class IPolicyEntryDeadLetterStrategy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryDeadLetterStrategyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryDeadLetterStrategy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryDeadLetterStrategy).__jsii_proxy_class__ = lambda : _IPolicyEntryDeadLetterStrategyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryDestination"
)
class IPolicyEntryDestination(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryDestinationProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryDestination"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryDestination).__jsii_proxy_class__ = lambda : _IPolicyEntryDestinationProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryDispatchPolicy"
)
class IPolicyEntryDispatchPolicy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryDispatchPolicyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryDispatchPolicy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryDispatchPolicy).__jsii_proxy_class__ = lambda : _IPolicyEntryDispatchPolicyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryMessageEvictionStrategy"
)
class IPolicyEntryMessageEvictionStrategy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryMessageEvictionStrategyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryMessageEvictionStrategy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryMessageEvictionStrategy).__jsii_proxy_class__ = lambda : _IPolicyEntryMessageEvictionStrategyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryMessageGroupMapFactory"
)
class IPolicyEntryMessageGroupMapFactory(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryMessageGroupMapFactoryProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryMessageGroupMapFactory"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryMessageGroupMapFactory).__jsii_proxy_class__ = lambda : _IPolicyEntryMessageGroupMapFactoryProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryPendingDurableSubscriberPolicy"
)
class IPolicyEntryPendingDurableSubscriberPolicy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryPendingDurableSubscriberPolicyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryPendingDurableSubscriberPolicy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryPendingDurableSubscriberPolicy).__jsii_proxy_class__ = lambda : _IPolicyEntryPendingDurableSubscriberPolicyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryPendingMessageLimitStrategy"
)
class IPolicyEntryPendingMessageLimitStrategy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryPendingMessageLimitStrategyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryPendingMessageLimitStrategy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryPendingMessageLimitStrategy).__jsii_proxy_class__ = lambda : _IPolicyEntryPendingMessageLimitStrategyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryPendingQueuePolicy"
)
class IPolicyEntryPendingQueuePolicy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryPendingQueuePolicyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryPendingQueuePolicy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryPendingQueuePolicy).__jsii_proxy_class__ = lambda : _IPolicyEntryPendingQueuePolicyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryPendingSubscriberPolicy"
)
class IPolicyEntryPendingSubscriberPolicy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntryPendingSubscriberPolicyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntryPendingSubscriberPolicy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntryPendingSubscriberPolicy).__jsii_proxy_class__ = lambda : _IPolicyEntryPendingSubscriberPolicyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntrySlowConsumerStrategy"
)
class IPolicyEntrySlowConsumerStrategy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntrySlowConsumerStrategyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntrySlowConsumerStrategy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntrySlowConsumerStrategy).__jsii_proxy_class__ = lambda : _IPolicyEntrySlowConsumerStrategyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntrySubscriptionRecoveryPolicy"
)
class IPolicyEntrySubscriptionRecoveryPolicy(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IPolicyEntrySubscriptionRecoveryPolicyProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IPolicyEntrySubscriptionRecoveryPolicy"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyEntrySubscriptionRecoveryPolicy).__jsii_proxy_class__ = lambda : _IPolicyEntrySubscriptionRecoveryPolicyProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IRetainedMessageSubscriptionRecoveryPolicyWrapped"
)
class IRetainedMessageSubscriptionRecoveryPolicyWrapped(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IRetainedMessageSubscriptionRecoveryPolicyWrappedProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IRetainedMessageSubscriptionRecoveryPolicyWrapped"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRetainedMessageSubscriptionRecoveryPolicyWrapped).__jsii_proxy_class__ = lambda : _IRetainedMessageSubscriptionRecoveryPolicyWrappedProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ISharedDeadLetterStrategyDeadLetterQueue"
)
class ISharedDeadLetterStrategyDeadLetterQueue(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _ISharedDeadLetterStrategyDeadLetterQueueProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ISharedDeadLetterStrategyDeadLetterQueue"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISharedDeadLetterStrategyDeadLetterQueue).__jsii_proxy_class__ = lambda : _ISharedDeadLetterStrategyDeadLetterQueueProxy


@jsii.interface(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IVirtualDestinationInterceptorVirtualDestination"
)
class IVirtualDestinationInterceptorVirtualDestination(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    pass


class _IVirtualDestinationInterceptorVirtualDestinationProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IVirtualDestinationInterceptorVirtualDestination"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualDestinationInterceptorVirtualDestination).__jsii_proxy_class__ = lambda : _IVirtualDestinationInterceptorVirtualDestinationProxy


@jsii.interface(jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IXmlNode")
class IXmlNode(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @jsii.member(jsii_name="toXmlString")
    def to_xml_string(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        ...


class _IXmlNodeProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IXmlNode"

    @jsii.member(jsii_name="toXmlString")
    def to_xml_string(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toXmlString", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IXmlNode).__jsii_proxy_class__ = lambda : _IXmlNodeProxy


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IndividualDeadLetterStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "destination_per_durable_subscriber": "destinationPerDurableSubscriber",
        "enable_audit": "enableAudit",
        "expiration": "expiration",
        "max_audit_depth": "maxAuditDepth",
        "max_producers_to_audit": "maxProducersToAudit",
        "process_expired": "processExpired",
        "process_non_persistent": "processNonPersistent",
        "queue_prefix": "queuePrefix",
        "queue_suffix": "queueSuffix",
        "topic_prefix": "topicPrefix",
        "topic_suffix": "topicSuffix",
        "use_queue_for_queue_messages": "useQueueForQueueMessages",
        "use_queue_for_topic_messages": "useQueueForTopicMessages",
    },
)
class IndividualDeadLetterStrategyAttributes:
    def __init__(
        self,
        *,
        destination_per_durable_subscriber: typing.Optional[builtins.bool] = None,
        enable_audit: typing.Optional[builtins.bool] = None,
        expiration: typing.Optional[jsii.Number] = None,
        max_audit_depth: typing.Optional[jsii.Number] = None,
        max_producers_to_audit: typing.Optional[jsii.Number] = None,
        process_expired: typing.Optional[builtins.bool] = None,
        process_non_persistent: typing.Optional[builtins.bool] = None,
        queue_prefix: typing.Optional[builtins.str] = None,
        queue_suffix: typing.Optional[builtins.str] = None,
        topic_prefix: typing.Optional[builtins.str] = None,
        topic_suffix: typing.Optional[builtins.str] = None,
        use_queue_for_queue_messages: typing.Optional[builtins.bool] = None,
        use_queue_for_topic_messages: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param destination_per_durable_subscriber: 
        :param enable_audit: 
        :param expiration: 
        :param max_audit_depth: 
        :param max_producers_to_audit: 
        :param process_expired: 
        :param process_non_persistent: 
        :param queue_prefix: 
        :param queue_suffix: 
        :param topic_prefix: 
        :param topic_suffix: 
        :param use_queue_for_queue_messages: 
        :param use_queue_for_topic_messages: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__396a1855177dac2190dfdd51d8590562a113154098f59346dd92adbd08db8b3e)
            check_type(argname="argument destination_per_durable_subscriber", value=destination_per_durable_subscriber, expected_type=type_hints["destination_per_durable_subscriber"])
            check_type(argname="argument enable_audit", value=enable_audit, expected_type=type_hints["enable_audit"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument max_audit_depth", value=max_audit_depth, expected_type=type_hints["max_audit_depth"])
            check_type(argname="argument max_producers_to_audit", value=max_producers_to_audit, expected_type=type_hints["max_producers_to_audit"])
            check_type(argname="argument process_expired", value=process_expired, expected_type=type_hints["process_expired"])
            check_type(argname="argument process_non_persistent", value=process_non_persistent, expected_type=type_hints["process_non_persistent"])
            check_type(argname="argument queue_prefix", value=queue_prefix, expected_type=type_hints["queue_prefix"])
            check_type(argname="argument queue_suffix", value=queue_suffix, expected_type=type_hints["queue_suffix"])
            check_type(argname="argument topic_prefix", value=topic_prefix, expected_type=type_hints["topic_prefix"])
            check_type(argname="argument topic_suffix", value=topic_suffix, expected_type=type_hints["topic_suffix"])
            check_type(argname="argument use_queue_for_queue_messages", value=use_queue_for_queue_messages, expected_type=type_hints["use_queue_for_queue_messages"])
            check_type(argname="argument use_queue_for_topic_messages", value=use_queue_for_topic_messages, expected_type=type_hints["use_queue_for_topic_messages"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination_per_durable_subscriber is not None:
            self._values["destination_per_durable_subscriber"] = destination_per_durable_subscriber
        if enable_audit is not None:
            self._values["enable_audit"] = enable_audit
        if expiration is not None:
            self._values["expiration"] = expiration
        if max_audit_depth is not None:
            self._values["max_audit_depth"] = max_audit_depth
        if max_producers_to_audit is not None:
            self._values["max_producers_to_audit"] = max_producers_to_audit
        if process_expired is not None:
            self._values["process_expired"] = process_expired
        if process_non_persistent is not None:
            self._values["process_non_persistent"] = process_non_persistent
        if queue_prefix is not None:
            self._values["queue_prefix"] = queue_prefix
        if queue_suffix is not None:
            self._values["queue_suffix"] = queue_suffix
        if topic_prefix is not None:
            self._values["topic_prefix"] = topic_prefix
        if topic_suffix is not None:
            self._values["topic_suffix"] = topic_suffix
        if use_queue_for_queue_messages is not None:
            self._values["use_queue_for_queue_messages"] = use_queue_for_queue_messages
        if use_queue_for_topic_messages is not None:
            self._values["use_queue_for_topic_messages"] = use_queue_for_topic_messages

    @builtins.property
    def destination_per_durable_subscriber(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("destination_per_durable_subscriber")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_audit(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("enable_audit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def expiration(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_audit_depth(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_audit_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_producers_to_audit(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_producers_to_audit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def process_expired(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("process_expired")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def process_non_persistent(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("process_non_persistent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def queue_prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queue_suffix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_suffix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_queue_for_queue_messages(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_queue_for_queue_messages")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_queue_for_topic_messages(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_queue_for_topic_messages")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IndividualDeadLetterStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.JournalDiskSyncStrategy"
)
class JournalDiskSyncStrategy(enum.Enum):
    '''
    :stability: experimental
    '''

    ALWAYS = "ALWAYS"
    '''
    :stability: experimental
    '''
    PERIODIC = "PERIODIC"
    '''
    :stability: experimental
    '''
    NEVER = "NEVER"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.KahaDBAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "checkpoint_interval": "checkpointInterval",
        "concurrent_store_and_dispatch_queues": "concurrentStoreAndDispatchQueues",
        "index_write_batch_size": "indexWriteBatchSize",
        "journal_disk_sync_interval": "journalDiskSyncInterval",
        "journal_disk_sync_strategy": "journalDiskSyncStrategy",
        "preallocation_strategy": "preallocationStrategy",
    },
)
class KahaDBAttributes:
    def __init__(
        self,
        *,
        checkpoint_interval: typing.Optional[jsii.Number] = None,
        concurrent_store_and_dispatch_queues: typing.Optional[builtins.bool] = None,
        index_write_batch_size: typing.Optional[jsii.Number] = None,
        journal_disk_sync_interval: typing.Optional[jsii.Number] = None,
        journal_disk_sync_strategy: typing.Optional[JournalDiskSyncStrategy] = None,
        preallocation_strategy: typing.Optional["PreallocationStrategy"] = None,
    ) -> None:
        '''
        :param checkpoint_interval: 
        :param concurrent_store_and_dispatch_queues: 
        :param index_write_batch_size: 
        :param journal_disk_sync_interval: 
        :param journal_disk_sync_strategy: 
        :param preallocation_strategy: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37d74e2c8f6462c9caa8fbd30b74bed2016110347400f38513b7d43726af521f)
            check_type(argname="argument checkpoint_interval", value=checkpoint_interval, expected_type=type_hints["checkpoint_interval"])
            check_type(argname="argument concurrent_store_and_dispatch_queues", value=concurrent_store_and_dispatch_queues, expected_type=type_hints["concurrent_store_and_dispatch_queues"])
            check_type(argname="argument index_write_batch_size", value=index_write_batch_size, expected_type=type_hints["index_write_batch_size"])
            check_type(argname="argument journal_disk_sync_interval", value=journal_disk_sync_interval, expected_type=type_hints["journal_disk_sync_interval"])
            check_type(argname="argument journal_disk_sync_strategy", value=journal_disk_sync_strategy, expected_type=type_hints["journal_disk_sync_strategy"])
            check_type(argname="argument preallocation_strategy", value=preallocation_strategy, expected_type=type_hints["preallocation_strategy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if checkpoint_interval is not None:
            self._values["checkpoint_interval"] = checkpoint_interval
        if concurrent_store_and_dispatch_queues is not None:
            self._values["concurrent_store_and_dispatch_queues"] = concurrent_store_and_dispatch_queues
        if index_write_batch_size is not None:
            self._values["index_write_batch_size"] = index_write_batch_size
        if journal_disk_sync_interval is not None:
            self._values["journal_disk_sync_interval"] = journal_disk_sync_interval
        if journal_disk_sync_strategy is not None:
            self._values["journal_disk_sync_strategy"] = journal_disk_sync_strategy
        if preallocation_strategy is not None:
            self._values["preallocation_strategy"] = preallocation_strategy

    @builtins.property
    def checkpoint_interval(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("checkpoint_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def concurrent_store_and_dispatch_queues(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("concurrent_store_and_dispatch_queues")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def index_write_batch_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("index_write_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def journal_disk_sync_interval(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("journal_disk_sync_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def journal_disk_sync_strategy(self) -> typing.Optional[JournalDiskSyncStrategy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("journal_disk_sync_strategy")
        return typing.cast(typing.Optional[JournalDiskSyncStrategy], result)

    @builtins.property
    def preallocation_strategy(self) -> typing.Optional["PreallocationStrategy"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("preallocation_strategy")
        return typing.cast(typing.Optional["PreallocationStrategy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KahaDBAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.MemoryUsageAttributes",
    jsii_struct_bases=[],
    name_mapping={"percent_of_jvm_heap": "percentOfJvmHeap"},
)
class MemoryUsageAttributes:
    def __init__(
        self,
        *,
        percent_of_jvm_heap: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param percent_of_jvm_heap: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4903e0e6089df5869a8182bbd41239c9eac8673cc37b35745b5833ac94659e6)
            check_type(argname="argument percent_of_jvm_heap", value=percent_of_jvm_heap, expected_type=type_hints["percent_of_jvm_heap"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if percent_of_jvm_heap is not None:
            self._values["percent_of_jvm_heap"] = percent_of_jvm_heap

    @builtins.property
    def percent_of_jvm_heap(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("percent_of_jvm_heap")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MemoryUsageAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.MessageGroupHashBucketFactoryAttributes",
    jsii_struct_bases=[],
    name_mapping={"bucket_count": "bucketCount", "cache_size": "cacheSize"},
)
class MessageGroupHashBucketFactoryAttributes:
    def __init__(
        self,
        *,
        bucket_count: typing.Optional[jsii.Number] = None,
        cache_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param bucket_count: 
        :param cache_size: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__095bcde135ae2bb2629ace626440c4dfd7fa593b2c59e0d1fe863eed4f69960d)
            check_type(argname="argument bucket_count", value=bucket_count, expected_type=type_hints["bucket_count"])
            check_type(argname="argument cache_size", value=cache_size, expected_type=type_hints["cache_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_count is not None:
            self._values["bucket_count"] = bucket_count
        if cache_size is not None:
            self._values["cache_size"] = cache_size

    @builtins.property
    def bucket_count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("bucket_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cache_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cache_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MessageGroupHashBucketFactoryAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.MirroredQueueAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "copy_message": "copyMessage",
        "postfix": "postfix",
        "prefix": "prefix",
    },
)
class MirroredQueueAttributes:
    def __init__(
        self,
        *,
        copy_message: typing.Optional[builtins.bool] = None,
        postfix: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param copy_message: 
        :param postfix: 
        :param prefix: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0987f07067169dcc392adce7a9a113038b882f4b48f5fdef1c06814eab139f6b)
            check_type(argname="argument copy_message", value=copy_message, expected_type=type_hints["copy_message"])
            check_type(argname="argument postfix", value=postfix, expected_type=type_hints["postfix"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if copy_message is not None:
            self._values["copy_message"] = copy_message
        if postfix is not None:
            self._values["postfix"] = postfix
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def copy_message(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("copy_message")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def postfix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("postfix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MirroredQueueAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.NetworkConnectorAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "advisory_ack_percentage": "advisoryAckPercentage",
        "advisory_for_failed_forward": "advisoryForFailedForward",
        "advisory_prefetch_size": "advisoryPrefetchSize",
        "always_sync_send": "alwaysSyncSend",
        "bridge_factory": "bridgeFactory",
        "bridge_temp_destinations": "bridgeTempDestinations",
        "broker_name": "brokerName",
        "broker_url": "brokerURL",
        "check_duplicate_messages_on_duplex": "checkDuplicateMessagesOnDuplex",
        "client_id_token": "clientIdToken",
        "conduit_network_queue_subscriptions": "conduitNetworkQueueSubscriptions",
        "conduit_subscriptions": "conduitSubscriptions",
        "connection_filter": "connectionFilter",
        "consumer_priority_base": "consumerPriorityBase",
        "consumer_ttl": "consumerTTL",
        "decrease_network_consumer_priority": "decreaseNetworkConsumerPriority",
        "destination_filter": "destinationFilter",
        "dispatch_async": "dispatchAsync",
        "duplex": "duplex",
        "dynamic_only": "dynamicOnly",
        "gc_destination_views": "gcDestinationViews",
        "gc_sweep_time": "gcSweepTime",
        "local_uri": "localUri",
        "message_ttl": "messageTTL",
        "name": "name",
        "network_ttl": "networkTTL",
        "object_name": "objectName",
        "prefetch_size": "prefetchSize",
        "static_bridge": "staticBridge",
        "suppress_duplicate_queue_subscriptions": "suppressDuplicateQueueSubscriptions",
        "suppress_duplicate_topic_subscriptions": "suppressDuplicateTopicSubscriptions",
        "sync_durable_subs": "syncDurableSubs",
        "uri": "uri",
        "use_broker_name_as_id_sees": "useBrokerNameAsIdSees",
        "use_compression": "useCompression",
        "user_name": "userName",
        "use_virtual_dest_subs": "useVirtualDestSubs",
    },
)
class NetworkConnectorAttributes:
    def __init__(
        self,
        *,
        advisory_ack_percentage: typing.Optional[jsii.Number] = None,
        advisory_for_failed_forward: typing.Optional[builtins.bool] = None,
        advisory_prefetch_size: typing.Optional[jsii.Number] = None,
        always_sync_send: typing.Optional[builtins.bool] = None,
        bridge_factory: typing.Optional[builtins.str] = None,
        bridge_temp_destinations: typing.Optional[builtins.bool] = None,
        broker_name: typing.Optional[builtins.str] = None,
        broker_url: typing.Optional[builtins.str] = None,
        check_duplicate_messages_on_duplex: typing.Optional[builtins.bool] = None,
        client_id_token: typing.Optional[builtins.str] = None,
        conduit_network_queue_subscriptions: typing.Optional[builtins.bool] = None,
        conduit_subscriptions: typing.Optional[builtins.bool] = None,
        connection_filter: typing.Optional[builtins.str] = None,
        consumer_priority_base: typing.Optional[jsii.Number] = None,
        consumer_ttl: typing.Optional[jsii.Number] = None,
        decrease_network_consumer_priority: typing.Optional[builtins.bool] = None,
        destination_filter: typing.Optional[builtins.str] = None,
        dispatch_async: typing.Optional[builtins.bool] = None,
        duplex: typing.Optional[builtins.bool] = None,
        dynamic_only: typing.Optional[builtins.bool] = None,
        gc_destination_views: typing.Optional[builtins.bool] = None,
        gc_sweep_time: typing.Optional[jsii.Number] = None,
        local_uri: typing.Optional[builtins.str] = None,
        message_ttl: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        network_ttl: typing.Optional[jsii.Number] = None,
        object_name: typing.Optional[builtins.str] = None,
        prefetch_size: typing.Optional[builtins.str] = None,
        static_bridge: typing.Optional[builtins.bool] = None,
        suppress_duplicate_queue_subscriptions: typing.Optional[builtins.bool] = None,
        suppress_duplicate_topic_subscriptions: typing.Optional[builtins.bool] = None,
        sync_durable_subs: typing.Optional[builtins.bool] = None,
        uri: typing.Optional[builtins.str] = None,
        use_broker_name_as_id_sees: typing.Optional[builtins.bool] = None,
        use_compression: typing.Optional[builtins.bool] = None,
        user_name: typing.Optional[builtins.str] = None,
        use_virtual_dest_subs: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param advisory_ack_percentage: 
        :param advisory_for_failed_forward: 
        :param advisory_prefetch_size: 
        :param always_sync_send: 
        :param bridge_factory: 
        :param bridge_temp_destinations: 
        :param broker_name: 
        :param broker_url: 
        :param check_duplicate_messages_on_duplex: 
        :param client_id_token: 
        :param conduit_network_queue_subscriptions: 
        :param conduit_subscriptions: 
        :param connection_filter: 
        :param consumer_priority_base: 
        :param consumer_ttl: 
        :param decrease_network_consumer_priority: 
        :param destination_filter: 
        :param dispatch_async: 
        :param duplex: 
        :param dynamic_only: 
        :param gc_destination_views: 
        :param gc_sweep_time: 
        :param local_uri: 
        :param message_ttl: 
        :param name: 
        :param network_ttl: 
        :param object_name: 
        :param prefetch_size: 
        :param static_bridge: 
        :param suppress_duplicate_queue_subscriptions: 
        :param suppress_duplicate_topic_subscriptions: 
        :param sync_durable_subs: 
        :param uri: 
        :param use_broker_name_as_id_sees: 
        :param use_compression: 
        :param user_name: 
        :param use_virtual_dest_subs: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ef8c92a358ac4ca23a18ff5996168f92d5b918c0dbd16ae115f0f3e51ae8a91)
            check_type(argname="argument advisory_ack_percentage", value=advisory_ack_percentage, expected_type=type_hints["advisory_ack_percentage"])
            check_type(argname="argument advisory_for_failed_forward", value=advisory_for_failed_forward, expected_type=type_hints["advisory_for_failed_forward"])
            check_type(argname="argument advisory_prefetch_size", value=advisory_prefetch_size, expected_type=type_hints["advisory_prefetch_size"])
            check_type(argname="argument always_sync_send", value=always_sync_send, expected_type=type_hints["always_sync_send"])
            check_type(argname="argument bridge_factory", value=bridge_factory, expected_type=type_hints["bridge_factory"])
            check_type(argname="argument bridge_temp_destinations", value=bridge_temp_destinations, expected_type=type_hints["bridge_temp_destinations"])
            check_type(argname="argument broker_name", value=broker_name, expected_type=type_hints["broker_name"])
            check_type(argname="argument broker_url", value=broker_url, expected_type=type_hints["broker_url"])
            check_type(argname="argument check_duplicate_messages_on_duplex", value=check_duplicate_messages_on_duplex, expected_type=type_hints["check_duplicate_messages_on_duplex"])
            check_type(argname="argument client_id_token", value=client_id_token, expected_type=type_hints["client_id_token"])
            check_type(argname="argument conduit_network_queue_subscriptions", value=conduit_network_queue_subscriptions, expected_type=type_hints["conduit_network_queue_subscriptions"])
            check_type(argname="argument conduit_subscriptions", value=conduit_subscriptions, expected_type=type_hints["conduit_subscriptions"])
            check_type(argname="argument connection_filter", value=connection_filter, expected_type=type_hints["connection_filter"])
            check_type(argname="argument consumer_priority_base", value=consumer_priority_base, expected_type=type_hints["consumer_priority_base"])
            check_type(argname="argument consumer_ttl", value=consumer_ttl, expected_type=type_hints["consumer_ttl"])
            check_type(argname="argument decrease_network_consumer_priority", value=decrease_network_consumer_priority, expected_type=type_hints["decrease_network_consumer_priority"])
            check_type(argname="argument destination_filter", value=destination_filter, expected_type=type_hints["destination_filter"])
            check_type(argname="argument dispatch_async", value=dispatch_async, expected_type=type_hints["dispatch_async"])
            check_type(argname="argument duplex", value=duplex, expected_type=type_hints["duplex"])
            check_type(argname="argument dynamic_only", value=dynamic_only, expected_type=type_hints["dynamic_only"])
            check_type(argname="argument gc_destination_views", value=gc_destination_views, expected_type=type_hints["gc_destination_views"])
            check_type(argname="argument gc_sweep_time", value=gc_sweep_time, expected_type=type_hints["gc_sweep_time"])
            check_type(argname="argument local_uri", value=local_uri, expected_type=type_hints["local_uri"])
            check_type(argname="argument message_ttl", value=message_ttl, expected_type=type_hints["message_ttl"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_ttl", value=network_ttl, expected_type=type_hints["network_ttl"])
            check_type(argname="argument object_name", value=object_name, expected_type=type_hints["object_name"])
            check_type(argname="argument prefetch_size", value=prefetch_size, expected_type=type_hints["prefetch_size"])
            check_type(argname="argument static_bridge", value=static_bridge, expected_type=type_hints["static_bridge"])
            check_type(argname="argument suppress_duplicate_queue_subscriptions", value=suppress_duplicate_queue_subscriptions, expected_type=type_hints["suppress_duplicate_queue_subscriptions"])
            check_type(argname="argument suppress_duplicate_topic_subscriptions", value=suppress_duplicate_topic_subscriptions, expected_type=type_hints["suppress_duplicate_topic_subscriptions"])
            check_type(argname="argument sync_durable_subs", value=sync_durable_subs, expected_type=type_hints["sync_durable_subs"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument use_broker_name_as_id_sees", value=use_broker_name_as_id_sees, expected_type=type_hints["use_broker_name_as_id_sees"])
            check_type(argname="argument use_compression", value=use_compression, expected_type=type_hints["use_compression"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument use_virtual_dest_subs", value=use_virtual_dest_subs, expected_type=type_hints["use_virtual_dest_subs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if advisory_ack_percentage is not None:
            self._values["advisory_ack_percentage"] = advisory_ack_percentage
        if advisory_for_failed_forward is not None:
            self._values["advisory_for_failed_forward"] = advisory_for_failed_forward
        if advisory_prefetch_size is not None:
            self._values["advisory_prefetch_size"] = advisory_prefetch_size
        if always_sync_send is not None:
            self._values["always_sync_send"] = always_sync_send
        if bridge_factory is not None:
            self._values["bridge_factory"] = bridge_factory
        if bridge_temp_destinations is not None:
            self._values["bridge_temp_destinations"] = bridge_temp_destinations
        if broker_name is not None:
            self._values["broker_name"] = broker_name
        if broker_url is not None:
            self._values["broker_url"] = broker_url
        if check_duplicate_messages_on_duplex is not None:
            self._values["check_duplicate_messages_on_duplex"] = check_duplicate_messages_on_duplex
        if client_id_token is not None:
            self._values["client_id_token"] = client_id_token
        if conduit_network_queue_subscriptions is not None:
            self._values["conduit_network_queue_subscriptions"] = conduit_network_queue_subscriptions
        if conduit_subscriptions is not None:
            self._values["conduit_subscriptions"] = conduit_subscriptions
        if connection_filter is not None:
            self._values["connection_filter"] = connection_filter
        if consumer_priority_base is not None:
            self._values["consumer_priority_base"] = consumer_priority_base
        if consumer_ttl is not None:
            self._values["consumer_ttl"] = consumer_ttl
        if decrease_network_consumer_priority is not None:
            self._values["decrease_network_consumer_priority"] = decrease_network_consumer_priority
        if destination_filter is not None:
            self._values["destination_filter"] = destination_filter
        if dispatch_async is not None:
            self._values["dispatch_async"] = dispatch_async
        if duplex is not None:
            self._values["duplex"] = duplex
        if dynamic_only is not None:
            self._values["dynamic_only"] = dynamic_only
        if gc_destination_views is not None:
            self._values["gc_destination_views"] = gc_destination_views
        if gc_sweep_time is not None:
            self._values["gc_sweep_time"] = gc_sweep_time
        if local_uri is not None:
            self._values["local_uri"] = local_uri
        if message_ttl is not None:
            self._values["message_ttl"] = message_ttl
        if name is not None:
            self._values["name"] = name
        if network_ttl is not None:
            self._values["network_ttl"] = network_ttl
        if object_name is not None:
            self._values["object_name"] = object_name
        if prefetch_size is not None:
            self._values["prefetch_size"] = prefetch_size
        if static_bridge is not None:
            self._values["static_bridge"] = static_bridge
        if suppress_duplicate_queue_subscriptions is not None:
            self._values["suppress_duplicate_queue_subscriptions"] = suppress_duplicate_queue_subscriptions
        if suppress_duplicate_topic_subscriptions is not None:
            self._values["suppress_duplicate_topic_subscriptions"] = suppress_duplicate_topic_subscriptions
        if sync_durable_subs is not None:
            self._values["sync_durable_subs"] = sync_durable_subs
        if uri is not None:
            self._values["uri"] = uri
        if use_broker_name_as_id_sees is not None:
            self._values["use_broker_name_as_id_sees"] = use_broker_name_as_id_sees
        if use_compression is not None:
            self._values["use_compression"] = use_compression
        if user_name is not None:
            self._values["user_name"] = user_name
        if use_virtual_dest_subs is not None:
            self._values["use_virtual_dest_subs"] = use_virtual_dest_subs

    @builtins.property
    def advisory_ack_percentage(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_ack_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def advisory_for_failed_forward(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_for_failed_forward")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def advisory_prefetch_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_prefetch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def always_sync_send(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("always_sync_send")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bridge_factory(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("bridge_factory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bridge_temp_destinations(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("bridge_temp_destinations")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def broker_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("broker_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def broker_url(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("broker_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def check_duplicate_messages_on_duplex(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("check_duplicate_messages_on_duplex")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def client_id_token(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("client_id_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conduit_network_queue_subscriptions(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("conduit_network_queue_subscriptions")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def conduit_subscriptions(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("conduit_subscriptions")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def connection_filter(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consumer_priority_base(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("consumer_priority_base")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consumer_ttl(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("consumer_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def decrease_network_consumer_priority(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("decrease_network_consumer_priority")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def destination_filter(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("destination_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dispatch_async(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dispatch_async")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def duplex(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("duplex")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dynamic_only(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dynamic_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def gc_destination_views(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("gc_destination_views")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def gc_sweep_time(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("gc_sweep_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def local_uri(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("local_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_ttl(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("message_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_ttl(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("network_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def object_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("object_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefetch_size(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefetch_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def static_bridge(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("static_bridge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def suppress_duplicate_queue_subscriptions(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("suppress_duplicate_queue_subscriptions")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def suppress_duplicate_topic_subscriptions(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("suppress_duplicate_topic_subscriptions")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sync_durable_subs(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("sync_durable_subs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_broker_name_as_id_sees(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_broker_name_as_id_sees")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_compression(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_compression")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_virtual_dest_subs(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_virtual_dest_subs")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectorAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.NetworkConnectorElements",
    jsii_struct_bases=[],
    name_mapping={
        "durable_destinations": "durableDestinations",
        "dynamically_included_destinations": "dynamicallyIncludedDestinations",
        "excluded_destinations": "excludedDestinations",
        "statically_included_destinations": "staticallyIncludedDestinations",
    },
)
class NetworkConnectorElements:
    def __init__(
        self,
        *,
        durable_destinations: typing.Optional[typing.Sequence[INetworkConnectorDurableDestination]] = None,
        dynamically_included_destinations: typing.Optional[typing.Sequence[INetworkConnectorDynamicallyIncludedDestination]] = None,
        excluded_destinations: typing.Optional[typing.Sequence[INetworkConnectorExcludedDestination]] = None,
        statically_included_destinations: typing.Optional[typing.Sequence[INetworkConnectorStaticallyIncludedDestination]] = None,
    ) -> None:
        '''
        :param durable_destinations: 
        :param dynamically_included_destinations: 
        :param excluded_destinations: 
        :param statically_included_destinations: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f7ad0a20e0a79768282f7582ba222192e38500452723755a8aeefdd97cf99e5)
            check_type(argname="argument durable_destinations", value=durable_destinations, expected_type=type_hints["durable_destinations"])
            check_type(argname="argument dynamically_included_destinations", value=dynamically_included_destinations, expected_type=type_hints["dynamically_included_destinations"])
            check_type(argname="argument excluded_destinations", value=excluded_destinations, expected_type=type_hints["excluded_destinations"])
            check_type(argname="argument statically_included_destinations", value=statically_included_destinations, expected_type=type_hints["statically_included_destinations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if durable_destinations is not None:
            self._values["durable_destinations"] = durable_destinations
        if dynamically_included_destinations is not None:
            self._values["dynamically_included_destinations"] = dynamically_included_destinations
        if excluded_destinations is not None:
            self._values["excluded_destinations"] = excluded_destinations
        if statically_included_destinations is not None:
            self._values["statically_included_destinations"] = statically_included_destinations

    @builtins.property
    def durable_destinations(
        self,
    ) -> typing.Optional[typing.List[INetworkConnectorDurableDestination]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("durable_destinations")
        return typing.cast(typing.Optional[typing.List[INetworkConnectorDurableDestination]], result)

    @builtins.property
    def dynamically_included_destinations(
        self,
    ) -> typing.Optional[typing.List[INetworkConnectorDynamicallyIncludedDestination]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dynamically_included_destinations")
        return typing.cast(typing.Optional[typing.List[INetworkConnectorDynamicallyIncludedDestination]], result)

    @builtins.property
    def excluded_destinations(
        self,
    ) -> typing.Optional[typing.List[INetworkConnectorExcludedDestination]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("excluded_destinations")
        return typing.cast(typing.Optional[typing.List[INetworkConnectorExcludedDestination]], result)

    @builtins.property
    def statically_included_destinations(
        self,
    ) -> typing.Optional[typing.List[INetworkConnectorStaticallyIncludedDestination]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("statically_included_destinations")
        return typing.cast(typing.Optional[typing.List[INetworkConnectorStaticallyIncludedDestination]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConnectorElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.OldestMessageEvictionStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "evict_expired_messages_high_watermark": "evictExpiredMessagesHighWatermark",
    },
)
class OldestMessageEvictionStrategyAttributes:
    def __init__(
        self,
        *,
        evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evict_expired_messages_high_watermark: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__348e1aac7b1b3a19d35c65856b1eb8b3c476e977b88ec7f2ebf7b3fa67cb554d)
            check_type(argname="argument evict_expired_messages_high_watermark", value=evict_expired_messages_high_watermark, expected_type=type_hints["evict_expired_messages_high_watermark"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if evict_expired_messages_high_watermark is not None:
            self._values["evict_expired_messages_high_watermark"] = evict_expired_messages_high_watermark

    @builtins.property
    def evict_expired_messages_high_watermark(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("evict_expired_messages_high_watermark")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OldestMessageEvictionStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.OldestMessageWithLowestPriorityEvictionStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "evict_expired_messages_high_watermark": "evictExpiredMessagesHighWatermark",
    },
)
class OldestMessageWithLowestPriorityEvictionStrategyAttributes:
    def __init__(
        self,
        *,
        evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evict_expired_messages_high_watermark: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49631d6f710fba8e428a2e8ac209a3468ad03fc65737c8eceb7c5769312c9f22)
            check_type(argname="argument evict_expired_messages_high_watermark", value=evict_expired_messages_high_watermark, expected_type=type_hints["evict_expired_messages_high_watermark"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if evict_expired_messages_high_watermark is not None:
            self._values["evict_expired_messages_high_watermark"] = evict_expired_messages_high_watermark

    @builtins.property
    def evict_expired_messages_high_watermark(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("evict_expired_messages_high_watermark")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OldestMessageWithLowestPriorityEvictionStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PolicyEntryAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "advisory_for_consumed": "advisoryForConsumed",
        "advisory_for_delivery": "advisoryForDelivery",
        "advisory_for_discarding_messages": "advisoryForDiscardingMessages",
        "advisory_for_fast_producers": "advisoryForFastProducers",
        "advisory_for_slow_consumers": "advisoryForSlowConsumers",
        "advisory_when_full": "advisoryWhenFull",
        "all_consumers_exclusive_by_default": "allConsumersExclusiveByDefault",
        "always_retroactive": "alwaysRetroactive",
        "blocked_producer_warning_interval": "blockedProducerWarningInterval",
        "consumers_before_dispatch_starts": "consumersBeforeDispatchStarts",
        "cursor_memory_high_water_mark": "cursorMemoryHighWaterMark",
        "do_optimze_message_storage": "doOptimzeMessageStorage",
        "durable_topic_prefetch": "durableTopicPrefetch",
        "enable_audit": "enableAudit",
        "expire_messages_period": "expireMessagesPeriod",
        "gc_inactive_destinations": "gcInactiveDestinations",
        "gc_with_network_consumers": "gcWithNetworkConsumers",
        "inactive_timeout_before_gc": "inactiveTimeoutBeforeGC",
        "inactive_timout_before_gc": "inactiveTimoutBeforeGC",
        "include_body_for_advisory": "includeBodyForAdvisory",
        "lazy_dispatch": "lazyDispatch",
        "max_audit_depth": "maxAuditDepth",
        "max_browse_page_size": "maxBrowsePageSize",
        "max_destinations": "maxDestinations",
        "max_expire_page_size": "maxExpirePageSize",
        "max_page_size": "maxPageSize",
        "max_producers_to_audit": "maxProducersToAudit",
        "max_queue_audit_depth": "maxQueueAuditDepth",
        "memory_limit": "memoryLimit",
        "message_group_map_factory_type": "messageGroupMapFactoryType",
        "minimum_message_size": "minimumMessageSize",
        "optimized_dispatch": "optimizedDispatch",
        "optimize_message_store_in_flight_limit": "optimizeMessageStoreInFlightLimit",
        "persist_jms_redelivered": "persistJMSRedelivered",
        "prioritized_messages": "prioritizedMessages",
        "producer_flow_control": "producerFlowControl",
        "queue": "queue",
        "queue_browser_prefetch": "queueBrowserPrefetch",
        "queue_prefetch": "queuePrefetch",
        "reduce_memory_footprint": "reduceMemoryFootprint",
        "send_advisory_if_no_consumers": "sendAdvisoryIfNoConsumers",
        "store_usage_high_water_mark": "storeUsageHighWaterMark",
        "strict_order_dispatch": "strictOrderDispatch",
        "temp_queue": "tempQueue",
        "temp_topic": "tempTopic",
        "time_before_dispatch_starts": "timeBeforeDispatchStarts",
        "topic": "topic",
        "topic_prefetch": "topicPrefetch",
        "use_cache": "useCache",
        "use_consumer_priority": "useConsumerPriority",
        "use_prefetch_extension": "usePrefetchExtension",
        "use_topic_subscription_inflight_stats": "useTopicSubscriptionInflightStats",
    },
)
class PolicyEntryAttributes:
    def __init__(
        self,
        *,
        advisory_for_consumed: typing.Optional[builtins.bool] = None,
        advisory_for_delivery: typing.Optional[builtins.bool] = None,
        advisory_for_discarding_messages: typing.Optional[builtins.bool] = None,
        advisory_for_fast_producers: typing.Optional[builtins.bool] = None,
        advisory_for_slow_consumers: typing.Optional[builtins.bool] = None,
        advisory_when_full: typing.Optional[builtins.bool] = None,
        all_consumers_exclusive_by_default: typing.Optional[builtins.bool] = None,
        always_retroactive: typing.Optional[builtins.bool] = None,
        blocked_producer_warning_interval: typing.Optional[jsii.Number] = None,
        consumers_before_dispatch_starts: typing.Optional[jsii.Number] = None,
        cursor_memory_high_water_mark: typing.Optional[jsii.Number] = None,
        do_optimze_message_storage: typing.Optional[builtins.bool] = None,
        durable_topic_prefetch: typing.Optional[jsii.Number] = None,
        enable_audit: typing.Optional[builtins.bool] = None,
        expire_messages_period: typing.Optional[jsii.Number] = None,
        gc_inactive_destinations: typing.Optional[builtins.bool] = None,
        gc_with_network_consumers: typing.Optional[builtins.bool] = None,
        inactive_timeout_before_gc: typing.Optional[jsii.Number] = None,
        inactive_timout_before_gc: typing.Optional[jsii.Number] = None,
        include_body_for_advisory: typing.Optional[builtins.bool] = None,
        lazy_dispatch: typing.Optional[builtins.bool] = None,
        max_audit_depth: typing.Optional[jsii.Number] = None,
        max_browse_page_size: typing.Optional[jsii.Number] = None,
        max_destinations: typing.Optional[jsii.Number] = None,
        max_expire_page_size: typing.Optional[jsii.Number] = None,
        max_page_size: typing.Optional[jsii.Number] = None,
        max_producers_to_audit: typing.Optional[jsii.Number] = None,
        max_queue_audit_depth: typing.Optional[jsii.Number] = None,
        memory_limit: typing.Optional[builtins.str] = None,
        message_group_map_factory_type: typing.Optional[builtins.str] = None,
        minimum_message_size: typing.Optional[jsii.Number] = None,
        optimized_dispatch: typing.Optional[builtins.bool] = None,
        optimize_message_store_in_flight_limit: typing.Optional[jsii.Number] = None,
        persist_jms_redelivered: typing.Optional[builtins.bool] = None,
        prioritized_messages: typing.Optional[builtins.bool] = None,
        producer_flow_control: typing.Optional[builtins.bool] = None,
        queue: typing.Optional[builtins.str] = None,
        queue_browser_prefetch: typing.Optional[jsii.Number] = None,
        queue_prefetch: typing.Optional[jsii.Number] = None,
        reduce_memory_footprint: typing.Optional[builtins.bool] = None,
        send_advisory_if_no_consumers: typing.Optional[builtins.bool] = None,
        store_usage_high_water_mark: typing.Optional[jsii.Number] = None,
        strict_order_dispatch: typing.Optional[builtins.bool] = None,
        temp_queue: typing.Optional[builtins.bool] = None,
        temp_topic: typing.Optional[builtins.bool] = None,
        time_before_dispatch_starts: typing.Optional[jsii.Number] = None,
        topic: typing.Optional[builtins.str] = None,
        topic_prefetch: typing.Optional[jsii.Number] = None,
        use_cache: typing.Optional[builtins.bool] = None,
        use_consumer_priority: typing.Optional[builtins.bool] = None,
        use_prefetch_extension: typing.Optional[builtins.bool] = None,
        use_topic_subscription_inflight_stats: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param advisory_for_consumed: 
        :param advisory_for_delivery: 
        :param advisory_for_discarding_messages: 
        :param advisory_for_fast_producers: 
        :param advisory_for_slow_consumers: 
        :param advisory_when_full: 
        :param all_consumers_exclusive_by_default: 
        :param always_retroactive: 
        :param blocked_producer_warning_interval: 
        :param consumers_before_dispatch_starts: 
        :param cursor_memory_high_water_mark: 
        :param do_optimze_message_storage: 
        :param durable_topic_prefetch: 
        :param enable_audit: 
        :param expire_messages_period: 
        :param gc_inactive_destinations: 
        :param gc_with_network_consumers: 
        :param inactive_timeout_before_gc: 
        :param inactive_timout_before_gc: 
        :param include_body_for_advisory: 
        :param lazy_dispatch: 
        :param max_audit_depth: 
        :param max_browse_page_size: 
        :param max_destinations: 
        :param max_expire_page_size: 
        :param max_page_size: 
        :param max_producers_to_audit: 
        :param max_queue_audit_depth: 
        :param memory_limit: 
        :param message_group_map_factory_type: 
        :param minimum_message_size: 
        :param optimized_dispatch: 
        :param optimize_message_store_in_flight_limit: 
        :param persist_jms_redelivered: 
        :param prioritized_messages: 
        :param producer_flow_control: 
        :param queue: 
        :param queue_browser_prefetch: 
        :param queue_prefetch: 
        :param reduce_memory_footprint: 
        :param send_advisory_if_no_consumers: 
        :param store_usage_high_water_mark: 
        :param strict_order_dispatch: 
        :param temp_queue: 
        :param temp_topic: 
        :param time_before_dispatch_starts: 
        :param topic: 
        :param topic_prefetch: 
        :param use_cache: 
        :param use_consumer_priority: 
        :param use_prefetch_extension: 
        :param use_topic_subscription_inflight_stats: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23c62a13be3fffdfc2d1295584eda7324f2e1566f73469ce4b3523eb2e2ec056)
            check_type(argname="argument advisory_for_consumed", value=advisory_for_consumed, expected_type=type_hints["advisory_for_consumed"])
            check_type(argname="argument advisory_for_delivery", value=advisory_for_delivery, expected_type=type_hints["advisory_for_delivery"])
            check_type(argname="argument advisory_for_discarding_messages", value=advisory_for_discarding_messages, expected_type=type_hints["advisory_for_discarding_messages"])
            check_type(argname="argument advisory_for_fast_producers", value=advisory_for_fast_producers, expected_type=type_hints["advisory_for_fast_producers"])
            check_type(argname="argument advisory_for_slow_consumers", value=advisory_for_slow_consumers, expected_type=type_hints["advisory_for_slow_consumers"])
            check_type(argname="argument advisory_when_full", value=advisory_when_full, expected_type=type_hints["advisory_when_full"])
            check_type(argname="argument all_consumers_exclusive_by_default", value=all_consumers_exclusive_by_default, expected_type=type_hints["all_consumers_exclusive_by_default"])
            check_type(argname="argument always_retroactive", value=always_retroactive, expected_type=type_hints["always_retroactive"])
            check_type(argname="argument blocked_producer_warning_interval", value=blocked_producer_warning_interval, expected_type=type_hints["blocked_producer_warning_interval"])
            check_type(argname="argument consumers_before_dispatch_starts", value=consumers_before_dispatch_starts, expected_type=type_hints["consumers_before_dispatch_starts"])
            check_type(argname="argument cursor_memory_high_water_mark", value=cursor_memory_high_water_mark, expected_type=type_hints["cursor_memory_high_water_mark"])
            check_type(argname="argument do_optimze_message_storage", value=do_optimze_message_storage, expected_type=type_hints["do_optimze_message_storage"])
            check_type(argname="argument durable_topic_prefetch", value=durable_topic_prefetch, expected_type=type_hints["durable_topic_prefetch"])
            check_type(argname="argument enable_audit", value=enable_audit, expected_type=type_hints["enable_audit"])
            check_type(argname="argument expire_messages_period", value=expire_messages_period, expected_type=type_hints["expire_messages_period"])
            check_type(argname="argument gc_inactive_destinations", value=gc_inactive_destinations, expected_type=type_hints["gc_inactive_destinations"])
            check_type(argname="argument gc_with_network_consumers", value=gc_with_network_consumers, expected_type=type_hints["gc_with_network_consumers"])
            check_type(argname="argument inactive_timeout_before_gc", value=inactive_timeout_before_gc, expected_type=type_hints["inactive_timeout_before_gc"])
            check_type(argname="argument inactive_timout_before_gc", value=inactive_timout_before_gc, expected_type=type_hints["inactive_timout_before_gc"])
            check_type(argname="argument include_body_for_advisory", value=include_body_for_advisory, expected_type=type_hints["include_body_for_advisory"])
            check_type(argname="argument lazy_dispatch", value=lazy_dispatch, expected_type=type_hints["lazy_dispatch"])
            check_type(argname="argument max_audit_depth", value=max_audit_depth, expected_type=type_hints["max_audit_depth"])
            check_type(argname="argument max_browse_page_size", value=max_browse_page_size, expected_type=type_hints["max_browse_page_size"])
            check_type(argname="argument max_destinations", value=max_destinations, expected_type=type_hints["max_destinations"])
            check_type(argname="argument max_expire_page_size", value=max_expire_page_size, expected_type=type_hints["max_expire_page_size"])
            check_type(argname="argument max_page_size", value=max_page_size, expected_type=type_hints["max_page_size"])
            check_type(argname="argument max_producers_to_audit", value=max_producers_to_audit, expected_type=type_hints["max_producers_to_audit"])
            check_type(argname="argument max_queue_audit_depth", value=max_queue_audit_depth, expected_type=type_hints["max_queue_audit_depth"])
            check_type(argname="argument memory_limit", value=memory_limit, expected_type=type_hints["memory_limit"])
            check_type(argname="argument message_group_map_factory_type", value=message_group_map_factory_type, expected_type=type_hints["message_group_map_factory_type"])
            check_type(argname="argument minimum_message_size", value=minimum_message_size, expected_type=type_hints["minimum_message_size"])
            check_type(argname="argument optimized_dispatch", value=optimized_dispatch, expected_type=type_hints["optimized_dispatch"])
            check_type(argname="argument optimize_message_store_in_flight_limit", value=optimize_message_store_in_flight_limit, expected_type=type_hints["optimize_message_store_in_flight_limit"])
            check_type(argname="argument persist_jms_redelivered", value=persist_jms_redelivered, expected_type=type_hints["persist_jms_redelivered"])
            check_type(argname="argument prioritized_messages", value=prioritized_messages, expected_type=type_hints["prioritized_messages"])
            check_type(argname="argument producer_flow_control", value=producer_flow_control, expected_type=type_hints["producer_flow_control"])
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
            check_type(argname="argument queue_browser_prefetch", value=queue_browser_prefetch, expected_type=type_hints["queue_browser_prefetch"])
            check_type(argname="argument queue_prefetch", value=queue_prefetch, expected_type=type_hints["queue_prefetch"])
            check_type(argname="argument reduce_memory_footprint", value=reduce_memory_footprint, expected_type=type_hints["reduce_memory_footprint"])
            check_type(argname="argument send_advisory_if_no_consumers", value=send_advisory_if_no_consumers, expected_type=type_hints["send_advisory_if_no_consumers"])
            check_type(argname="argument store_usage_high_water_mark", value=store_usage_high_water_mark, expected_type=type_hints["store_usage_high_water_mark"])
            check_type(argname="argument strict_order_dispatch", value=strict_order_dispatch, expected_type=type_hints["strict_order_dispatch"])
            check_type(argname="argument temp_queue", value=temp_queue, expected_type=type_hints["temp_queue"])
            check_type(argname="argument temp_topic", value=temp_topic, expected_type=type_hints["temp_topic"])
            check_type(argname="argument time_before_dispatch_starts", value=time_before_dispatch_starts, expected_type=type_hints["time_before_dispatch_starts"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument topic_prefetch", value=topic_prefetch, expected_type=type_hints["topic_prefetch"])
            check_type(argname="argument use_cache", value=use_cache, expected_type=type_hints["use_cache"])
            check_type(argname="argument use_consumer_priority", value=use_consumer_priority, expected_type=type_hints["use_consumer_priority"])
            check_type(argname="argument use_prefetch_extension", value=use_prefetch_extension, expected_type=type_hints["use_prefetch_extension"])
            check_type(argname="argument use_topic_subscription_inflight_stats", value=use_topic_subscription_inflight_stats, expected_type=type_hints["use_topic_subscription_inflight_stats"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if advisory_for_consumed is not None:
            self._values["advisory_for_consumed"] = advisory_for_consumed
        if advisory_for_delivery is not None:
            self._values["advisory_for_delivery"] = advisory_for_delivery
        if advisory_for_discarding_messages is not None:
            self._values["advisory_for_discarding_messages"] = advisory_for_discarding_messages
        if advisory_for_fast_producers is not None:
            self._values["advisory_for_fast_producers"] = advisory_for_fast_producers
        if advisory_for_slow_consumers is not None:
            self._values["advisory_for_slow_consumers"] = advisory_for_slow_consumers
        if advisory_when_full is not None:
            self._values["advisory_when_full"] = advisory_when_full
        if all_consumers_exclusive_by_default is not None:
            self._values["all_consumers_exclusive_by_default"] = all_consumers_exclusive_by_default
        if always_retroactive is not None:
            self._values["always_retroactive"] = always_retroactive
        if blocked_producer_warning_interval is not None:
            self._values["blocked_producer_warning_interval"] = blocked_producer_warning_interval
        if consumers_before_dispatch_starts is not None:
            self._values["consumers_before_dispatch_starts"] = consumers_before_dispatch_starts
        if cursor_memory_high_water_mark is not None:
            self._values["cursor_memory_high_water_mark"] = cursor_memory_high_water_mark
        if do_optimze_message_storage is not None:
            self._values["do_optimze_message_storage"] = do_optimze_message_storage
        if durable_topic_prefetch is not None:
            self._values["durable_topic_prefetch"] = durable_topic_prefetch
        if enable_audit is not None:
            self._values["enable_audit"] = enable_audit
        if expire_messages_period is not None:
            self._values["expire_messages_period"] = expire_messages_period
        if gc_inactive_destinations is not None:
            self._values["gc_inactive_destinations"] = gc_inactive_destinations
        if gc_with_network_consumers is not None:
            self._values["gc_with_network_consumers"] = gc_with_network_consumers
        if inactive_timeout_before_gc is not None:
            self._values["inactive_timeout_before_gc"] = inactive_timeout_before_gc
        if inactive_timout_before_gc is not None:
            self._values["inactive_timout_before_gc"] = inactive_timout_before_gc
        if include_body_for_advisory is not None:
            self._values["include_body_for_advisory"] = include_body_for_advisory
        if lazy_dispatch is not None:
            self._values["lazy_dispatch"] = lazy_dispatch
        if max_audit_depth is not None:
            self._values["max_audit_depth"] = max_audit_depth
        if max_browse_page_size is not None:
            self._values["max_browse_page_size"] = max_browse_page_size
        if max_destinations is not None:
            self._values["max_destinations"] = max_destinations
        if max_expire_page_size is not None:
            self._values["max_expire_page_size"] = max_expire_page_size
        if max_page_size is not None:
            self._values["max_page_size"] = max_page_size
        if max_producers_to_audit is not None:
            self._values["max_producers_to_audit"] = max_producers_to_audit
        if max_queue_audit_depth is not None:
            self._values["max_queue_audit_depth"] = max_queue_audit_depth
        if memory_limit is not None:
            self._values["memory_limit"] = memory_limit
        if message_group_map_factory_type is not None:
            self._values["message_group_map_factory_type"] = message_group_map_factory_type
        if minimum_message_size is not None:
            self._values["minimum_message_size"] = minimum_message_size
        if optimized_dispatch is not None:
            self._values["optimized_dispatch"] = optimized_dispatch
        if optimize_message_store_in_flight_limit is not None:
            self._values["optimize_message_store_in_flight_limit"] = optimize_message_store_in_flight_limit
        if persist_jms_redelivered is not None:
            self._values["persist_jms_redelivered"] = persist_jms_redelivered
        if prioritized_messages is not None:
            self._values["prioritized_messages"] = prioritized_messages
        if producer_flow_control is not None:
            self._values["producer_flow_control"] = producer_flow_control
        if queue is not None:
            self._values["queue"] = queue
        if queue_browser_prefetch is not None:
            self._values["queue_browser_prefetch"] = queue_browser_prefetch
        if queue_prefetch is not None:
            self._values["queue_prefetch"] = queue_prefetch
        if reduce_memory_footprint is not None:
            self._values["reduce_memory_footprint"] = reduce_memory_footprint
        if send_advisory_if_no_consumers is not None:
            self._values["send_advisory_if_no_consumers"] = send_advisory_if_no_consumers
        if store_usage_high_water_mark is not None:
            self._values["store_usage_high_water_mark"] = store_usage_high_water_mark
        if strict_order_dispatch is not None:
            self._values["strict_order_dispatch"] = strict_order_dispatch
        if temp_queue is not None:
            self._values["temp_queue"] = temp_queue
        if temp_topic is not None:
            self._values["temp_topic"] = temp_topic
        if time_before_dispatch_starts is not None:
            self._values["time_before_dispatch_starts"] = time_before_dispatch_starts
        if topic is not None:
            self._values["topic"] = topic
        if topic_prefetch is not None:
            self._values["topic_prefetch"] = topic_prefetch
        if use_cache is not None:
            self._values["use_cache"] = use_cache
        if use_consumer_priority is not None:
            self._values["use_consumer_priority"] = use_consumer_priority
        if use_prefetch_extension is not None:
            self._values["use_prefetch_extension"] = use_prefetch_extension
        if use_topic_subscription_inflight_stats is not None:
            self._values["use_topic_subscription_inflight_stats"] = use_topic_subscription_inflight_stats

    @builtins.property
    def advisory_for_consumed(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_for_consumed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def advisory_for_delivery(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_for_delivery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def advisory_for_discarding_messages(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_for_discarding_messages")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def advisory_for_fast_producers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_for_fast_producers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def advisory_for_slow_consumers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_for_slow_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def advisory_when_full(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("advisory_when_full")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def all_consumers_exclusive_by_default(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("all_consumers_exclusive_by_default")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def always_retroactive(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("always_retroactive")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def blocked_producer_warning_interval(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("blocked_producer_warning_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consumers_before_dispatch_starts(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("consumers_before_dispatch_starts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cursor_memory_high_water_mark(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cursor_memory_high_water_mark")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def do_optimze_message_storage(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("do_optimze_message_storage")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def durable_topic_prefetch(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("durable_topic_prefetch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_audit(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("enable_audit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def expire_messages_period(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("expire_messages_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def gc_inactive_destinations(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("gc_inactive_destinations")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def gc_with_network_consumers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("gc_with_network_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def inactive_timeout_before_gc(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("inactive_timeout_before_gc")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def inactive_timout_before_gc(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("inactive_timout_before_gc")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def include_body_for_advisory(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("include_body_for_advisory")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def lazy_dispatch(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lazy_dispatch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_audit_depth(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_audit_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_browse_page_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_browse_page_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_destinations(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_destinations")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_expire_page_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_expire_page_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_page_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_page_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_producers_to_audit(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_producers_to_audit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_queue_audit_depth(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_queue_audit_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_limit(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("memory_limit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_group_map_factory_type(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("message_group_map_factory_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_message_size(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("minimum_message_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def optimized_dispatch(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("optimized_dispatch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def optimize_message_store_in_flight_limit(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("optimize_message_store_in_flight_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def persist_jms_redelivered(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("persist_jms_redelivered")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def prioritized_messages(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prioritized_messages")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def producer_flow_control(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("producer_flow_control")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def queue(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queue_browser_prefetch(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue_browser_prefetch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def queue_prefetch(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue_prefetch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def reduce_memory_footprint(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("reduce_memory_footprint")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def send_advisory_if_no_consumers(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("send_advisory_if_no_consumers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def store_usage_high_water_mark(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("store_usage_high_water_mark")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strict_order_dispatch(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("strict_order_dispatch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def temp_queue(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_queue")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def temp_topic(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_topic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def time_before_dispatch_starts(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("time_before_dispatch_starts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_prefetch(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic_prefetch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_cache(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_cache")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_consumer_priority(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_consumer_priority")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_prefetch_extension(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_prefetch_extension")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_topic_subscription_inflight_stats(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_topic_subscription_inflight_stats")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyEntryAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PolicyEntryElements",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_strategy": "deadLetterStrategy",
        "destination": "destination",
        "dispatch_policy": "dispatchPolicy",
        "message_eviction_strategy": "messageEvictionStrategy",
        "message_group_map_factory": "messageGroupMapFactory",
        "network_bridge_filter_factory": "networkBridgeFilterFactory",
        "pending_durable_subscriber_policy": "pendingDurableSubscriberPolicy",
        "pending_message_limit_strategy": "pendingMessageLimitStrategy",
        "pending_queue_policy": "pendingQueuePolicy",
        "pending_subscriber_policy": "pendingSubscriberPolicy",
        "slow_consumer_strategy": "slowConsumerStrategy",
        "subscription_recovery_policy": "subscriptionRecoveryPolicy",
    },
)
class PolicyEntryElements:
    def __init__(
        self,
        *,
        dead_letter_strategy: typing.Optional[IPolicyEntryDeadLetterStrategy] = None,
        destination: typing.Optional[IPolicyEntryDestination] = None,
        dispatch_policy: typing.Optional[IPolicyEntryDispatchPolicy] = None,
        message_eviction_strategy: typing.Optional[IPolicyEntryMessageEvictionStrategy] = None,
        message_group_map_factory: typing.Optional[IPolicyEntryMessageGroupMapFactory] = None,
        network_bridge_filter_factory: typing.Optional["ConditionalNetworkBridgeFilterFactory"] = None,
        pending_durable_subscriber_policy: typing.Optional[IPolicyEntryPendingDurableSubscriberPolicy] = None,
        pending_message_limit_strategy: typing.Optional[IPolicyEntryPendingMessageLimitStrategy] = None,
        pending_queue_policy: typing.Optional[IPolicyEntryPendingQueuePolicy] = None,
        pending_subscriber_policy: typing.Optional[IPolicyEntryPendingSubscriberPolicy] = None,
        slow_consumer_strategy: typing.Optional[IPolicyEntrySlowConsumerStrategy] = None,
        subscription_recovery_policy: typing.Optional[IPolicyEntrySubscriptionRecoveryPolicy] = None,
    ) -> None:
        '''
        :param dead_letter_strategy: 
        :param destination: 
        :param dispatch_policy: 
        :param message_eviction_strategy: 
        :param message_group_map_factory: 
        :param network_bridge_filter_factory: 
        :param pending_durable_subscriber_policy: 
        :param pending_message_limit_strategy: 
        :param pending_queue_policy: 
        :param pending_subscriber_policy: 
        :param slow_consumer_strategy: 
        :param subscription_recovery_policy: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b16a938162f792e6f035ab637529ca7ab2155f46a84e5ebb7ecdcb401142d82c)
            check_type(argname="argument dead_letter_strategy", value=dead_letter_strategy, expected_type=type_hints["dead_letter_strategy"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument dispatch_policy", value=dispatch_policy, expected_type=type_hints["dispatch_policy"])
            check_type(argname="argument message_eviction_strategy", value=message_eviction_strategy, expected_type=type_hints["message_eviction_strategy"])
            check_type(argname="argument message_group_map_factory", value=message_group_map_factory, expected_type=type_hints["message_group_map_factory"])
            check_type(argname="argument network_bridge_filter_factory", value=network_bridge_filter_factory, expected_type=type_hints["network_bridge_filter_factory"])
            check_type(argname="argument pending_durable_subscriber_policy", value=pending_durable_subscriber_policy, expected_type=type_hints["pending_durable_subscriber_policy"])
            check_type(argname="argument pending_message_limit_strategy", value=pending_message_limit_strategy, expected_type=type_hints["pending_message_limit_strategy"])
            check_type(argname="argument pending_queue_policy", value=pending_queue_policy, expected_type=type_hints["pending_queue_policy"])
            check_type(argname="argument pending_subscriber_policy", value=pending_subscriber_policy, expected_type=type_hints["pending_subscriber_policy"])
            check_type(argname="argument slow_consumer_strategy", value=slow_consumer_strategy, expected_type=type_hints["slow_consumer_strategy"])
            check_type(argname="argument subscription_recovery_policy", value=subscription_recovery_policy, expected_type=type_hints["subscription_recovery_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_strategy is not None:
            self._values["dead_letter_strategy"] = dead_letter_strategy
        if destination is not None:
            self._values["destination"] = destination
        if dispatch_policy is not None:
            self._values["dispatch_policy"] = dispatch_policy
        if message_eviction_strategy is not None:
            self._values["message_eviction_strategy"] = message_eviction_strategy
        if message_group_map_factory is not None:
            self._values["message_group_map_factory"] = message_group_map_factory
        if network_bridge_filter_factory is not None:
            self._values["network_bridge_filter_factory"] = network_bridge_filter_factory
        if pending_durable_subscriber_policy is not None:
            self._values["pending_durable_subscriber_policy"] = pending_durable_subscriber_policy
        if pending_message_limit_strategy is not None:
            self._values["pending_message_limit_strategy"] = pending_message_limit_strategy
        if pending_queue_policy is not None:
            self._values["pending_queue_policy"] = pending_queue_policy
        if pending_subscriber_policy is not None:
            self._values["pending_subscriber_policy"] = pending_subscriber_policy
        if slow_consumer_strategy is not None:
            self._values["slow_consumer_strategy"] = slow_consumer_strategy
        if subscription_recovery_policy is not None:
            self._values["subscription_recovery_policy"] = subscription_recovery_policy

    @builtins.property
    def dead_letter_strategy(self) -> typing.Optional[IPolicyEntryDeadLetterStrategy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dead_letter_strategy")
        return typing.cast(typing.Optional[IPolicyEntryDeadLetterStrategy], result)

    @builtins.property
    def destination(self) -> typing.Optional[IPolicyEntryDestination]:
        '''
        :stability: experimental
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[IPolicyEntryDestination], result)

    @builtins.property
    def dispatch_policy(self) -> typing.Optional[IPolicyEntryDispatchPolicy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dispatch_policy")
        return typing.cast(typing.Optional[IPolicyEntryDispatchPolicy], result)

    @builtins.property
    def message_eviction_strategy(
        self,
    ) -> typing.Optional[IPolicyEntryMessageEvictionStrategy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("message_eviction_strategy")
        return typing.cast(typing.Optional[IPolicyEntryMessageEvictionStrategy], result)

    @builtins.property
    def message_group_map_factory(
        self,
    ) -> typing.Optional[IPolicyEntryMessageGroupMapFactory]:
        '''
        :stability: experimental
        '''
        result = self._values.get("message_group_map_factory")
        return typing.cast(typing.Optional[IPolicyEntryMessageGroupMapFactory], result)

    @builtins.property
    def network_bridge_filter_factory(
        self,
    ) -> typing.Optional["ConditionalNetworkBridgeFilterFactory"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("network_bridge_filter_factory")
        return typing.cast(typing.Optional["ConditionalNetworkBridgeFilterFactory"], result)

    @builtins.property
    def pending_durable_subscriber_policy(
        self,
    ) -> typing.Optional[IPolicyEntryPendingDurableSubscriberPolicy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("pending_durable_subscriber_policy")
        return typing.cast(typing.Optional[IPolicyEntryPendingDurableSubscriberPolicy], result)

    @builtins.property
    def pending_message_limit_strategy(
        self,
    ) -> typing.Optional[IPolicyEntryPendingMessageLimitStrategy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("pending_message_limit_strategy")
        return typing.cast(typing.Optional[IPolicyEntryPendingMessageLimitStrategy], result)

    @builtins.property
    def pending_queue_policy(self) -> typing.Optional[IPolicyEntryPendingQueuePolicy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("pending_queue_policy")
        return typing.cast(typing.Optional[IPolicyEntryPendingQueuePolicy], result)

    @builtins.property
    def pending_subscriber_policy(
        self,
    ) -> typing.Optional[IPolicyEntryPendingSubscriberPolicy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("pending_subscriber_policy")
        return typing.cast(typing.Optional[IPolicyEntryPendingSubscriberPolicy], result)

    @builtins.property
    def slow_consumer_strategy(
        self,
    ) -> typing.Optional[IPolicyEntrySlowConsumerStrategy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("slow_consumer_strategy")
        return typing.cast(typing.Optional[IPolicyEntrySlowConsumerStrategy], result)

    @builtins.property
    def subscription_recovery_policy(
        self,
    ) -> typing.Optional[IPolicyEntrySubscriptionRecoveryPolicy]:
        '''
        :stability: experimental
        '''
        result = self._values.get("subscription_recovery_policy")
        return typing.cast(typing.Optional[IPolicyEntrySubscriptionRecoveryPolicy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyEntryElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PolicyMapElements",
    jsii_struct_bases=[],
    name_mapping={"default_entry": "defaultEntry", "policy_entries": "policyEntries"},
)
class PolicyMapElements:
    def __init__(
        self,
        *,
        default_entry: typing.Optional["PolicyEntry"] = None,
        policy_entries: typing.Optional[typing.Sequence["PolicyEntry"]] = None,
    ) -> None:
        '''
        :param default_entry: 
        :param policy_entries: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce613069539bf302c4cdee3cd46342316ebc47bb4e02daf50547a701ef7fbd29)
            check_type(argname="argument default_entry", value=default_entry, expected_type=type_hints["default_entry"])
            check_type(argname="argument policy_entries", value=policy_entries, expected_type=type_hints["policy_entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_entry is not None:
            self._values["default_entry"] = default_entry
        if policy_entries is not None:
            self._values["policy_entries"] = policy_entries

    @builtins.property
    def default_entry(self) -> typing.Optional["PolicyEntry"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("default_entry")
        return typing.cast(typing.Optional["PolicyEntry"], result)

    @builtins.property
    def policy_entries(self) -> typing.Optional[typing.List["PolicyEntry"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("policy_entries")
        return typing.cast(typing.Optional[typing.List["PolicyEntry"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyMapElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PreallocationStrategy"
)
class PreallocationStrategy(enum.Enum):
    '''
    :stability: experimental
    '''

    SPARSE_FILE = "SPARSE_FILE"
    '''
    :stability: experimental
    '''
    OS_KERNEL_COPY = "OS_KERNEL_COPY"
    '''
    :stability: experimental
    '''
    ZEROS = "ZEROS"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PrefetchRatePendingMessageLimitStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={"multiplier": "multiplier"},
)
class PrefetchRatePendingMessageLimitStrategyAttributes:
    def __init__(self, *, multiplier: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param multiplier: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc6a31f34c1ca729699b2e5e65f940317bdd647631da7b5c49a03f9ad05f4d47)
            check_type(argname="argument multiplier", value=multiplier, expected_type=type_hints["multiplier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if multiplier is not None:
            self._values["multiplier"] = multiplier

    @builtins.property
    def multiplier(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("multiplier")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrefetchRatePendingMessageLimitStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.Protocol")
class Protocol(enum.Enum):
    '''
    :stability: experimental
    '''

    OPENWIRE = "OPENWIRE"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.QueryBasedSubscriptionRecoveryPolicyAttributes",
    jsii_struct_bases=[],
    name_mapping={"query": "query"},
)
class QueryBasedSubscriptionRecoveryPolicyAttributes:
    def __init__(self, *, query: typing.Optional[builtins.str] = None) -> None:
        '''
        :param query: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__520edbc8a2e4d132d95ebe20421298a7d5cdb1697ef3e391029deae70ba9d22c)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if query is not None:
            self._values["query"] = query

    @builtins.property
    def query(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueryBasedSubscriptionRecoveryPolicyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.QueueAttributes",
    jsii_struct_bases=[],
    name_mapping={"dlq": "dlq", "physical_name": "physicalName"},
)
class QueueAttributes:
    def __init__(
        self,
        *,
        dlq: typing.Optional[builtins.bool] = None,
        physical_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dlq: 
        :param physical_name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045a61d5c821ac7d87c756a997288dc98ba7614227b1f8e03a255a27c764f623)
            check_type(argname="argument dlq", value=dlq, expected_type=type_hints["dlq"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dlq is not None:
            self._values["dlq"] = dlq
        if physical_name is not None:
            self._values["physical_name"] = physical_name

    @builtins.property
    def dlq(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dlq")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def physical_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("physical_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RedeliveryPluginAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "fallback_to_dead_letter": "fallbackToDeadLetter",
        "send_to_dlq_if_max_retries_exceeded": "sendToDlqIfMaxRetriesExceeded",
    },
)
class RedeliveryPluginAttributes:
    def __init__(
        self,
        *,
        fallback_to_dead_letter: typing.Optional[builtins.bool] = None,
        send_to_dlq_if_max_retries_exceeded: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param fallback_to_dead_letter: 
        :param send_to_dlq_if_max_retries_exceeded: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0c06cf42b3a16ae312438524e15ab844665cfdade59df885a2d8c79090c62a4)
            check_type(argname="argument fallback_to_dead_letter", value=fallback_to_dead_letter, expected_type=type_hints["fallback_to_dead_letter"])
            check_type(argname="argument send_to_dlq_if_max_retries_exceeded", value=send_to_dlq_if_max_retries_exceeded, expected_type=type_hints["send_to_dlq_if_max_retries_exceeded"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fallback_to_dead_letter is not None:
            self._values["fallback_to_dead_letter"] = fallback_to_dead_letter
        if send_to_dlq_if_max_retries_exceeded is not None:
            self._values["send_to_dlq_if_max_retries_exceeded"] = send_to_dlq_if_max_retries_exceeded

    @builtins.property
    def fallback_to_dead_letter(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("fallback_to_dead_letter")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def send_to_dlq_if_max_retries_exceeded(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("send_to_dlq_if_max_retries_exceeded")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedeliveryPluginAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RedeliveryPluginElements",
    jsii_struct_bases=[],
    name_mapping={"redelivery_policy_map": "redeliveryPolicyMap"},
)
class RedeliveryPluginElements:
    def __init__(
        self,
        *,
        redelivery_policy_map: typing.Optional["RedeliveryPolicyMap"] = None,
    ) -> None:
        '''
        :param redelivery_policy_map: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f36395bd5901ad6ac98438f1fc43289f3d11c59fa5c04643683667d111c50f07)
            check_type(argname="argument redelivery_policy_map", value=redelivery_policy_map, expected_type=type_hints["redelivery_policy_map"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if redelivery_policy_map is not None:
            self._values["redelivery_policy_map"] = redelivery_policy_map

    @builtins.property
    def redelivery_policy_map(self) -> typing.Optional["RedeliveryPolicyMap"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("redelivery_policy_map")
        return typing.cast(typing.Optional["RedeliveryPolicyMap"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedeliveryPluginElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RedeliveryPolicyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "back_off_multiplier": "backOffMultiplier",
        "collision_avoidance_percent": "collisionAvoidancePercent",
        "initial_redelivery_delay": "initialRedeliveryDelay",
        "maximum_redeliveries": "maximumRedeliveries",
        "maximum_redelivery_delay": "maximumRedeliveryDelay",
        "pre_dispatch_check": "preDispatchCheck",
        "queue": "queue",
        "redelivery_delay": "redeliveryDelay",
        "temp_queue": "tempQueue",
        "temp_topic": "tempTopic",
        "topic": "topic",
        "use_collision_avoidance": "useCollisionAvoidance",
        "use_exponential_back_off": "useExponentialBackOff",
    },
)
class RedeliveryPolicyAttributes:
    def __init__(
        self,
        *,
        back_off_multiplier: typing.Optional[jsii.Number] = None,
        collision_avoidance_percent: typing.Optional[jsii.Number] = None,
        initial_redelivery_delay: typing.Optional[jsii.Number] = None,
        maximum_redeliveries: typing.Optional[jsii.Number] = None,
        maximum_redelivery_delay: typing.Optional[jsii.Number] = None,
        pre_dispatch_check: typing.Optional[builtins.bool] = None,
        queue: typing.Optional[builtins.str] = None,
        redelivery_delay: typing.Optional[jsii.Number] = None,
        temp_queue: typing.Optional[builtins.bool] = None,
        temp_topic: typing.Optional[builtins.bool] = None,
        topic: typing.Optional[builtins.str] = None,
        use_collision_avoidance: typing.Optional[builtins.bool] = None,
        use_exponential_back_off: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param back_off_multiplier: 
        :param collision_avoidance_percent: 
        :param initial_redelivery_delay: 
        :param maximum_redeliveries: 
        :param maximum_redelivery_delay: 
        :param pre_dispatch_check: 
        :param queue: 
        :param redelivery_delay: 
        :param temp_queue: 
        :param temp_topic: 
        :param topic: 
        :param use_collision_avoidance: 
        :param use_exponential_back_off: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6077886a71c12977282d30fc5f0b51f19aae5ac7885822c2a50f7a35528f2ba3)
            check_type(argname="argument back_off_multiplier", value=back_off_multiplier, expected_type=type_hints["back_off_multiplier"])
            check_type(argname="argument collision_avoidance_percent", value=collision_avoidance_percent, expected_type=type_hints["collision_avoidance_percent"])
            check_type(argname="argument initial_redelivery_delay", value=initial_redelivery_delay, expected_type=type_hints["initial_redelivery_delay"])
            check_type(argname="argument maximum_redeliveries", value=maximum_redeliveries, expected_type=type_hints["maximum_redeliveries"])
            check_type(argname="argument maximum_redelivery_delay", value=maximum_redelivery_delay, expected_type=type_hints["maximum_redelivery_delay"])
            check_type(argname="argument pre_dispatch_check", value=pre_dispatch_check, expected_type=type_hints["pre_dispatch_check"])
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
            check_type(argname="argument redelivery_delay", value=redelivery_delay, expected_type=type_hints["redelivery_delay"])
            check_type(argname="argument temp_queue", value=temp_queue, expected_type=type_hints["temp_queue"])
            check_type(argname="argument temp_topic", value=temp_topic, expected_type=type_hints["temp_topic"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument use_collision_avoidance", value=use_collision_avoidance, expected_type=type_hints["use_collision_avoidance"])
            check_type(argname="argument use_exponential_back_off", value=use_exponential_back_off, expected_type=type_hints["use_exponential_back_off"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if back_off_multiplier is not None:
            self._values["back_off_multiplier"] = back_off_multiplier
        if collision_avoidance_percent is not None:
            self._values["collision_avoidance_percent"] = collision_avoidance_percent
        if initial_redelivery_delay is not None:
            self._values["initial_redelivery_delay"] = initial_redelivery_delay
        if maximum_redeliveries is not None:
            self._values["maximum_redeliveries"] = maximum_redeliveries
        if maximum_redelivery_delay is not None:
            self._values["maximum_redelivery_delay"] = maximum_redelivery_delay
        if pre_dispatch_check is not None:
            self._values["pre_dispatch_check"] = pre_dispatch_check
        if queue is not None:
            self._values["queue"] = queue
        if redelivery_delay is not None:
            self._values["redelivery_delay"] = redelivery_delay
        if temp_queue is not None:
            self._values["temp_queue"] = temp_queue
        if temp_topic is not None:
            self._values["temp_topic"] = temp_topic
        if topic is not None:
            self._values["topic"] = topic
        if use_collision_avoidance is not None:
            self._values["use_collision_avoidance"] = use_collision_avoidance
        if use_exponential_back_off is not None:
            self._values["use_exponential_back_off"] = use_exponential_back_off

    @builtins.property
    def back_off_multiplier(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("back_off_multiplier")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def collision_avoidance_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("collision_avoidance_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_redelivery_delay(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("initial_redelivery_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_redeliveries(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("maximum_redeliveries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_redelivery_delay(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("maximum_redelivery_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pre_dispatch_check(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("pre_dispatch_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def queue(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redelivery_delay(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("redelivery_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def temp_queue(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_queue")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def temp_topic(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_topic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_collision_avoidance(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_collision_avoidance")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_exponential_back_off(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_exponential_back_off")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedeliveryPolicyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RedeliveryPolicyMapElements",
    jsii_struct_bases=[],
    name_mapping={
        "default_entry": "defaultEntry",
        "redelivery_policy_entries": "redeliveryPolicyEntries",
    },
)
class RedeliveryPolicyMapElements:
    def __init__(
        self,
        *,
        default_entry: typing.Optional["RedeliveryPolicy"] = None,
        redelivery_policy_entries: typing.Optional[typing.Sequence["RedeliveryPolicy"]] = None,
    ) -> None:
        '''
        :param default_entry: 
        :param redelivery_policy_entries: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb2ba699d1c8d6e98011cdf67a67e81d54863850137e50644259c74430e4feb1)
            check_type(argname="argument default_entry", value=default_entry, expected_type=type_hints["default_entry"])
            check_type(argname="argument redelivery_policy_entries", value=redelivery_policy_entries, expected_type=type_hints["redelivery_policy_entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_entry is not None:
            self._values["default_entry"] = default_entry
        if redelivery_policy_entries is not None:
            self._values["redelivery_policy_entries"] = redelivery_policy_entries

    @builtins.property
    def default_entry(self) -> typing.Optional["RedeliveryPolicy"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("default_entry")
        return typing.cast(typing.Optional["RedeliveryPolicy"], result)

    @builtins.property
    def redelivery_policy_entries(
        self,
    ) -> typing.Optional[typing.List["RedeliveryPolicy"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("redelivery_policy_entries")
        return typing.cast(typing.Optional[typing.List["RedeliveryPolicy"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedeliveryPolicyMapElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RetainedMessageSubscriptionRecoveryPolicyElements",
    jsii_struct_bases=[],
    name_mapping={"wrapped": "wrapped"},
)
class RetainedMessageSubscriptionRecoveryPolicyElements:
    def __init__(
        self,
        *,
        wrapped: typing.Optional[IRetainedMessageSubscriptionRecoveryPolicyWrapped] = None,
    ) -> None:
        '''
        :param wrapped: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0453478659ff4daa1aa92da51caa58f8bb3b0ccaf13faf912c640a7f4d6b3f9a)
            check_type(argname="argument wrapped", value=wrapped, expected_type=type_hints["wrapped"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if wrapped is not None:
            self._values["wrapped"] = wrapped

    @builtins.property
    def wrapped(
        self,
    ) -> typing.Optional[IRetainedMessageSubscriptionRecoveryPolicyWrapped]:
        '''
        :stability: experimental
        '''
        result = self._values.get("wrapped")
        return typing.cast(typing.Optional[IRetainedMessageSubscriptionRecoveryPolicyWrapped], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RetainedMessageSubscriptionRecoveryPolicyElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.SharedDeadLetterStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "enable_audit": "enableAudit",
        "expiration": "expiration",
        "max_audit_depth": "maxAuditDepth",
        "max_producers_to_audit": "maxProducersToAudit",
        "process_expired": "processExpired",
        "process_non_persistent": "processNonPersistent",
    },
)
class SharedDeadLetterStrategyAttributes:
    def __init__(
        self,
        *,
        enable_audit: typing.Optional[builtins.bool] = None,
        expiration: typing.Optional[jsii.Number] = None,
        max_audit_depth: typing.Optional[jsii.Number] = None,
        max_producers_to_audit: typing.Optional[jsii.Number] = None,
        process_expired: typing.Optional[builtins.bool] = None,
        process_non_persistent: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param enable_audit: 
        :param expiration: 
        :param max_audit_depth: 
        :param max_producers_to_audit: 
        :param process_expired: 
        :param process_non_persistent: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f87807482f477573540ab9243bf742280b9611fc889ba8c3c9f9c6f311efc4a)
            check_type(argname="argument enable_audit", value=enable_audit, expected_type=type_hints["enable_audit"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument max_audit_depth", value=max_audit_depth, expected_type=type_hints["max_audit_depth"])
            check_type(argname="argument max_producers_to_audit", value=max_producers_to_audit, expected_type=type_hints["max_producers_to_audit"])
            check_type(argname="argument process_expired", value=process_expired, expected_type=type_hints["process_expired"])
            check_type(argname="argument process_non_persistent", value=process_non_persistent, expected_type=type_hints["process_non_persistent"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enable_audit is not None:
            self._values["enable_audit"] = enable_audit
        if expiration is not None:
            self._values["expiration"] = expiration
        if max_audit_depth is not None:
            self._values["max_audit_depth"] = max_audit_depth
        if max_producers_to_audit is not None:
            self._values["max_producers_to_audit"] = max_producers_to_audit
        if process_expired is not None:
            self._values["process_expired"] = process_expired
        if process_non_persistent is not None:
            self._values["process_non_persistent"] = process_non_persistent

    @builtins.property
    def enable_audit(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("enable_audit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def expiration(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_audit_depth(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_audit_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_producers_to_audit(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("max_producers_to_audit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def process_expired(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("process_expired")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def process_non_persistent(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("process_non_persistent")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SharedDeadLetterStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.SharedDeadLetterStrategyElements",
    jsii_struct_bases=[],
    name_mapping={"dead_letter_queue": "deadLetterQueue"},
)
class SharedDeadLetterStrategyElements:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[ISharedDeadLetterStrategyDeadLetterQueue] = None,
    ) -> None:
        '''
        :param dead_letter_queue: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f63014b243db8d09966f65c9a1dea54fca5915ea5a8cfca673bede4dcf8cf59f)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue

    @builtins.property
    def dead_letter_queue(
        self,
    ) -> typing.Optional[ISharedDeadLetterStrategyDeadLetterQueue]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[ISharedDeadLetterStrategyDeadLetterQueue], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SharedDeadLetterStrategyElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.StoreDurableSubscriberCursorAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "immediate_priority_dispatch": "immediatePriorityDispatch",
        "use_cache": "useCache",
    },
)
class StoreDurableSubscriberCursorAttributes:
    def __init__(
        self,
        *,
        immediate_priority_dispatch: typing.Optional[builtins.bool] = None,
        use_cache: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param immediate_priority_dispatch: 
        :param use_cache: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__593afe7700b49120eeacfdc39f20b1737c31e796cf5c0fba83340dabeef3f38c)
            check_type(argname="argument immediate_priority_dispatch", value=immediate_priority_dispatch, expected_type=type_hints["immediate_priority_dispatch"])
            check_type(argname="argument use_cache", value=use_cache, expected_type=type_hints["use_cache"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if immediate_priority_dispatch is not None:
            self._values["immediate_priority_dispatch"] = immediate_priority_dispatch
        if use_cache is not None:
            self._values["use_cache"] = use_cache

    @builtins.property
    def immediate_priority_dispatch(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("immediate_priority_dispatch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_cache(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("use_cache")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoreDurableSubscriberCursorAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.SystemUsageAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "send_fail_if_no_space": "sendFailIfNoSpace",
        "send_fail_if_no_space_after_timeout": "sendFailIfNoSpaceAfterTimeout",
    },
)
class SystemUsageAttributes:
    def __init__(
        self,
        *,
        send_fail_if_no_space: typing.Optional[builtins.bool] = None,
        send_fail_if_no_space_after_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param send_fail_if_no_space: 
        :param send_fail_if_no_space_after_timeout: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0376a5d92919815b5da10fc9118724a951cc73c3fa2f4558445606e509c6fc8)
            check_type(argname="argument send_fail_if_no_space", value=send_fail_if_no_space, expected_type=type_hints["send_fail_if_no_space"])
            check_type(argname="argument send_fail_if_no_space_after_timeout", value=send_fail_if_no_space_after_timeout, expected_type=type_hints["send_fail_if_no_space_after_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if send_fail_if_no_space is not None:
            self._values["send_fail_if_no_space"] = send_fail_if_no_space
        if send_fail_if_no_space_after_timeout is not None:
            self._values["send_fail_if_no_space_after_timeout"] = send_fail_if_no_space_after_timeout

    @builtins.property
    def send_fail_if_no_space(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("send_fail_if_no_space")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def send_fail_if_no_space_after_timeout(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("send_fail_if_no_space_after_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SystemUsageAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.SystemUsageElements",
    jsii_struct_bases=[],
    name_mapping={"memory_usage": "memoryUsage"},
)
class SystemUsageElements:
    def __init__(self, *, memory_usage: typing.Optional["MemoryUsage"] = None) -> None:
        '''
        :param memory_usage: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4350699e0199c9c74281c8e4a718389b7996a7b013c831ac023d780de0519611)
            check_type(argname="argument memory_usage", value=memory_usage, expected_type=type_hints["memory_usage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if memory_usage is not None:
            self._values["memory_usage"] = memory_usage

    @builtins.property
    def memory_usage(self) -> typing.Optional["MemoryUsage"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("memory_usage")
        return typing.cast(typing.Optional["MemoryUsage"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SystemUsageElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TempDestinationAuthorizationEntryAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "admin": "admin",
        "queue": "queue",
        "read": "read",
        "temp_queue": "tempQueue",
        "temp_topic": "tempTopic",
        "topic": "topic",
        "write": "write",
    },
)
class TempDestinationAuthorizationEntryAttributes:
    def __init__(
        self,
        *,
        admin: typing.Optional[builtins.str] = None,
        queue: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        temp_queue: typing.Optional[builtins.bool] = None,
        temp_topic: typing.Optional[builtins.bool] = None,
        topic: typing.Optional[builtins.str] = None,
        write: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin: 
        :param queue: 
        :param read: 
        :param temp_queue: 
        :param temp_topic: 
        :param topic: 
        :param write: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__095b0872f3a3448d73eb4d8e7ad935cbbc66c8a59d882a9f21dc0bd8418589d2)
            check_type(argname="argument admin", value=admin, expected_type=type_hints["admin"])
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument temp_queue", value=temp_queue, expected_type=type_hints["temp_queue"])
            check_type(argname="argument temp_topic", value=temp_topic, expected_type=type_hints["temp_topic"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument write", value=write, expected_type=type_hints["write"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if admin is not None:
            self._values["admin"] = admin
        if queue is not None:
            self._values["queue"] = queue
        if read is not None:
            self._values["read"] = read
        if temp_queue is not None:
            self._values["temp_queue"] = temp_queue
        if temp_topic is not None:
            self._values["temp_topic"] = temp_topic
        if topic is not None:
            self._values["topic"] = topic
        if write is not None:
            self._values["write"] = write

    @builtins.property
    def admin(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("admin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queue(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def temp_queue(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_queue")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def temp_topic(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("temp_topic")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def topic(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("write")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TempDestinationAuthorizationEntryAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TempQueueAttributes",
    jsii_struct_bases=[],
    name_mapping={"dlq": "dlq", "physical_name": "physicalName"},
)
class TempQueueAttributes:
    def __init__(
        self,
        *,
        dlq: typing.Optional[builtins.bool] = None,
        physical_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dlq: 
        :param physical_name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78e7c188346ee36d099526b16714598cf80f5e8576d2eb36c6c543d3ecfa835d)
            check_type(argname="argument dlq", value=dlq, expected_type=type_hints["dlq"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dlq is not None:
            self._values["dlq"] = dlq
        if physical_name is not None:
            self._values["physical_name"] = physical_name

    @builtins.property
    def dlq(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dlq")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def physical_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("physical_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TempQueueAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TempTopicAttributes",
    jsii_struct_bases=[],
    name_mapping={"dlq": "dlq", "physical_name": "physicalName"},
)
class TempTopicAttributes:
    def __init__(
        self,
        *,
        dlq: typing.Optional[builtins.bool] = None,
        physical_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dlq: 
        :param physical_name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca6a3d63d19b7ccaf3a3be05b53ee63eb3f97fbb929cbf05474afecf829c9dfb)
            check_type(argname="argument dlq", value=dlq, expected_type=type_hints["dlq"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dlq is not None:
            self._values["dlq"] = dlq
        if physical_name is not None:
            self._values["physical_name"] = physical_name

    @builtins.property
    def dlq(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dlq")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def physical_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("physical_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TempTopicAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TimeStampingBrokerPluginAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "future_only": "futureOnly",
        "process_network_messages": "processNetworkMessages",
        "ttl_ceiling": "ttlCeiling",
        "zero_expiration_override": "zeroExpirationOverride",
    },
)
class TimeStampingBrokerPluginAttributes:
    def __init__(
        self,
        *,
        future_only: typing.Optional[builtins.bool] = None,
        process_network_messages: typing.Optional[builtins.bool] = None,
        ttl_ceiling: typing.Optional[jsii.Number] = None,
        zero_expiration_override: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param future_only: 
        :param process_network_messages: 
        :param ttl_ceiling: 
        :param zero_expiration_override: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a51728b5cffbed4dddb97fa340ac96b66764c7a34eafa7b0dd53e9b4d4233cf)
            check_type(argname="argument future_only", value=future_only, expected_type=type_hints["future_only"])
            check_type(argname="argument process_network_messages", value=process_network_messages, expected_type=type_hints["process_network_messages"])
            check_type(argname="argument ttl_ceiling", value=ttl_ceiling, expected_type=type_hints["ttl_ceiling"])
            check_type(argname="argument zero_expiration_override", value=zero_expiration_override, expected_type=type_hints["zero_expiration_override"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if future_only is not None:
            self._values["future_only"] = future_only
        if process_network_messages is not None:
            self._values["process_network_messages"] = process_network_messages
        if ttl_ceiling is not None:
            self._values["ttl_ceiling"] = ttl_ceiling
        if zero_expiration_override is not None:
            self._values["zero_expiration_override"] = zero_expiration_override

    @builtins.property
    def future_only(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("future_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def process_network_messages(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("process_network_messages")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ttl_ceiling(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("ttl_ceiling")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zero_expiration_override(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("zero_expiration_override")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimeStampingBrokerPluginAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TimedSubscriptionRecoveryPolicyAttributes",
    jsii_struct_bases=[],
    name_mapping={"recover_duration": "recoverDuration"},
)
class TimedSubscriptionRecoveryPolicyAttributes:
    def __init__(
        self,
        *,
        recover_duration: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param recover_duration: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2182c1329a941a479e79d04f110f2c1edc4e3f3fd1cca777ace1e909336a589)
            check_type(argname="argument recover_duration", value=recover_duration, expected_type=type_hints["recover_duration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if recover_duration is not None:
            self._values["recover_duration"] = recover_duration

    @builtins.property
    def recover_duration(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("recover_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimedSubscriptionRecoveryPolicyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TopicAttributes",
    jsii_struct_bases=[],
    name_mapping={"dlq": "dlq", "physical_name": "physicalName"},
)
class TopicAttributes:
    def __init__(
        self,
        *,
        dlq: typing.Optional[builtins.bool] = None,
        physical_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dlq: 
        :param physical_name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16300f6db82cccf9a732d65ed21ce94e15b6b1c333c7fbe72776903eebff319f)
            check_type(argname="argument dlq", value=dlq, expected_type=type_hints["dlq"])
            check_type(argname="argument physical_name", value=physical_name, expected_type=type_hints["physical_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dlq is not None:
            self._values["dlq"] = dlq
        if physical_name is not None:
            self._values["physical_name"] = physical_name

    @builtins.property
    def dlq(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dlq")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def physical_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("physical_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TransportConnectorAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "rebalance_cluster_clients": "rebalanceClusterClients",
        "update_cluster_clients": "updateClusterClients",
        "update_cluster_clients_on_remove": "updateClusterClientsOnRemove",
    },
)
class TransportConnectorAttributes:
    def __init__(
        self,
        *,
        name: typing.Optional[Protocol] = None,
        rebalance_cluster_clients: typing.Optional[builtins.bool] = None,
        update_cluster_clients: typing.Optional[builtins.bool] = None,
        update_cluster_clients_on_remove: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param name: 
        :param rebalance_cluster_clients: 
        :param update_cluster_clients: 
        :param update_cluster_clients_on_remove: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7baea1cf102b98da3ea85cc1e67aa836d7d8df137de74c177a25fc41240c3ff)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rebalance_cluster_clients", value=rebalance_cluster_clients, expected_type=type_hints["rebalance_cluster_clients"])
            check_type(argname="argument update_cluster_clients", value=update_cluster_clients, expected_type=type_hints["update_cluster_clients"])
            check_type(argname="argument update_cluster_clients_on_remove", value=update_cluster_clients_on_remove, expected_type=type_hints["update_cluster_clients_on_remove"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if rebalance_cluster_clients is not None:
            self._values["rebalance_cluster_clients"] = rebalance_cluster_clients
        if update_cluster_clients is not None:
            self._values["update_cluster_clients"] = update_cluster_clients
        if update_cluster_clients_on_remove is not None:
            self._values["update_cluster_clients_on_remove"] = update_cluster_clients_on_remove

    @builtins.property
    def name(self) -> typing.Optional[Protocol]:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[Protocol], result)

    @builtins.property
    def rebalance_cluster_clients(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("rebalance_cluster_clients")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def update_cluster_clients(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("update_cluster_clients")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def update_cluster_clients_on_remove(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("update_cluster_clients_on_remove")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransportConnectorAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.UniquePropertyMessageEvictionStrategyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "evict_expired_messages_high_watermark": "evictExpiredMessagesHighWatermark",
        "property_name": "propertyName",
    },
)
class UniquePropertyMessageEvictionStrategyAttributes:
    def __init__(
        self,
        *,
        evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
        property_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evict_expired_messages_high_watermark: 
        :param property_name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08109f7f0746dc91f300f10996517ff42b15d1de294910e8d359b9d495ad77ea)
            check_type(argname="argument evict_expired_messages_high_watermark", value=evict_expired_messages_high_watermark, expected_type=type_hints["evict_expired_messages_high_watermark"])
            check_type(argname="argument property_name", value=property_name, expected_type=type_hints["property_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if evict_expired_messages_high_watermark is not None:
            self._values["evict_expired_messages_high_watermark"] = evict_expired_messages_high_watermark
        if property_name is not None:
            self._values["property_name"] = property_name

    @builtins.property
    def evict_expired_messages_high_watermark(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("evict_expired_messages_high_watermark")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def property_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("property_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UniquePropertyMessageEvictionStrategyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.VirtualDestinationInterceptorElements",
    jsii_struct_bases=[],
    name_mapping={"virtual_destinations": "virtualDestinations"},
)
class VirtualDestinationInterceptorElements:
    def __init__(
        self,
        *,
        virtual_destinations: typing.Sequence[IVirtualDestinationInterceptorVirtualDestination],
    ) -> None:
        '''
        :param virtual_destinations: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63aa66ce16f478861859efa0e94b3fca2a0b743b4732997ce7616882ba25b086)
            check_type(argname="argument virtual_destinations", value=virtual_destinations, expected_type=type_hints["virtual_destinations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_destinations": virtual_destinations,
        }

    @builtins.property
    def virtual_destinations(
        self,
    ) -> typing.List[IVirtualDestinationInterceptorVirtualDestination]:
        '''
        :stability: experimental
        '''
        result = self._values.get("virtual_destinations")
        assert result is not None, "Required property 'virtual_destinations' is missing"
        return typing.cast(typing.List[IVirtualDestinationInterceptorVirtualDestination], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualDestinationInterceptorElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.VirtualTopicAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "concurrent_send": "concurrentSend",
        "local": "local",
        "name": "name",
        "postfix": "postfix",
        "prefix": "prefix",
        "selector_aware": "selectorAware",
        "transacted_send": "transactedSend",
    },
)
class VirtualTopicAttributes:
    def __init__(
        self,
        *,
        concurrent_send: typing.Optional[builtins.bool] = None,
        local: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        postfix: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        selector_aware: typing.Optional[builtins.bool] = None,
        transacted_send: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param concurrent_send: 
        :param local: 
        :param name: 
        :param postfix: 
        :param prefix: 
        :param selector_aware: 
        :param transacted_send: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7248d19f987267d0f2e2a874b04e72d00a9f08f457a4135c2d60773e385ba2e5)
            check_type(argname="argument concurrent_send", value=concurrent_send, expected_type=type_hints["concurrent_send"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument postfix", value=postfix, expected_type=type_hints["postfix"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument selector_aware", value=selector_aware, expected_type=type_hints["selector_aware"])
            check_type(argname="argument transacted_send", value=transacted_send, expected_type=type_hints["transacted_send"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if concurrent_send is not None:
            self._values["concurrent_send"] = concurrent_send
        if local is not None:
            self._values["local"] = local
        if name is not None:
            self._values["name"] = name
        if postfix is not None:
            self._values["postfix"] = postfix
        if prefix is not None:
            self._values["prefix"] = prefix
        if selector_aware is not None:
            self._values["selector_aware"] = selector_aware
        if transacted_send is not None:
            self._values["transacted_send"] = transacted_send

    @builtins.property
    def concurrent_send(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("concurrent_send")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def local(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postfix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("postfix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selector_aware(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("selector_aware")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def transacted_send(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("transacted_send")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualTopicAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IXmlNode)
class XmlNode(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.XmlNode",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        attrs_names_overrides: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elems_names_overrides: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        tag_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attrs_names_overrides: 
        :param elems_names_overrides: 
        :param namespace: 
        :param tag_name: 

        :stability: experimental
        '''
        props = XmlNodeProps(
            attrs_names_overrides=attrs_names_overrides,
            elems_names_overrides=elems_names_overrides,
            namespace=namespace,
            tag_name=tag_name,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toXmlString")
    def to_xml_string(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toXmlString", []))


@jsii.data_type(
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.XmlNodeProps",
    jsii_struct_bases=[],
    name_mapping={
        "attrs_names_overrides": "attrsNamesOverrides",
        "elems_names_overrides": "elemsNamesOverrides",
        "namespace": "namespace",
        "tag_name": "tagName",
    },
)
class XmlNodeProps:
    def __init__(
        self,
        *,
        attrs_names_overrides: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elems_names_overrides: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        tag_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attrs_names_overrides: 
        :param elems_names_overrides: 
        :param namespace: 
        :param tag_name: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8321b03ee93c02e7e07dfd82974dd0f3ce3ade6e8bdd528c0877ec782b6d5c4)
            check_type(argname="argument attrs_names_overrides", value=attrs_names_overrides, expected_type=type_hints["attrs_names_overrides"])
            check_type(argname="argument elems_names_overrides", value=elems_names_overrides, expected_type=type_hints["elems_names_overrides"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument tag_name", value=tag_name, expected_type=type_hints["tag_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if attrs_names_overrides is not None:
            self._values["attrs_names_overrides"] = attrs_names_overrides
        if elems_names_overrides is not None:
            self._values["elems_names_overrides"] = elems_names_overrides
        if namespace is not None:
            self._values["namespace"] = namespace
        if tag_name is not None:
            self._values["tag_name"] = tag_name

    @builtins.property
    def attrs_names_overrides(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("attrs_names_overrides")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def elems_names_overrides(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("elems_names_overrides")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("tag_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XmlNodeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPolicyEntrySlowConsumerStrategy)
class AbortSlowAckConsumerStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AbortSlowAckConsumerStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        abort_connection: typing.Optional[builtins.bool] = None,
        check_period: typing.Optional[jsii.Number] = None,
        ignore_idle_consumers: typing.Optional[builtins.bool] = None,
        ignore_network_consumers: typing.Optional[builtins.bool] = None,
        max_slow_count: typing.Optional[jsii.Number] = None,
        max_slow_duration: typing.Optional[jsii.Number] = None,
        max_time_since_last_ack: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param abort_connection: 
        :param check_period: 
        :param ignore_idle_consumers: 
        :param ignore_network_consumers: 
        :param max_slow_count: 
        :param max_slow_duration: 
        :param max_time_since_last_ack: 
        :param name: 

        :stability: experimental
        '''
        attributes = AbortSlowAckConsumerStrategyAttributes(
            abort_connection=abort_connection,
            check_period=check_period,
            ignore_idle_consumers=ignore_idle_consumers,
            ignore_network_consumers=ignore_network_consumers,
            max_slow_count=max_slow_count,
            max_slow_duration=max_slow_duration,
            max_time_since_last_ack=max_time_since_last_ack,
            name=name,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[AbortSlowAckConsumerStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[AbortSlowAckConsumerStrategyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntrySlowConsumerStrategy)
class AbortSlowConsumerStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AbortSlowConsumerStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        abort_connection: typing.Optional[builtins.bool] = None,
        check_period: typing.Optional[jsii.Number] = None,
        ignore_network_consumers: typing.Optional[builtins.bool] = None,
        max_slow_count: typing.Optional[jsii.Number] = None,
        max_slow_duration: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param abort_connection: 
        :param check_period: 
        :param ignore_network_consumers: 
        :param max_slow_count: 
        :param max_slow_duration: 
        :param name: 

        :stability: experimental
        '''
        attributes = AbortSlowConsumerStrategyAttributes(
            abort_connection=abort_connection,
            check_period=check_period,
            ignore_network_consumers=ignore_network_consumers,
            max_slow_count=max_slow_count,
            max_slow_duration=max_slow_duration,
            name=name,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[AbortSlowConsumerStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[AbortSlowConsumerStrategyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IAuthorizationMapAuthorizationEntry, IAuthorizationMapDefaultEntry)
class AuthorizationEntry(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AuthorizationEntry",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        admin: typing.Optional[builtins.str] = None,
        queue: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        temp_queue: typing.Optional[builtins.bool] = None,
        temp_topic: typing.Optional[builtins.bool] = None,
        topic: typing.Optional[builtins.str] = None,
        write: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin: 
        :param queue: 
        :param read: 
        :param temp_queue: 
        :param temp_topic: 
        :param topic: 
        :param write: 

        :stability: experimental
        '''
        attributes = AuthorizationEntryAttributes(
            admin=admin,
            queue=queue,
            read=read,
            temp_queue=temp_queue,
            temp_topic=temp_topic,
            topic=topic,
            write=write,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[AuthorizationEntryAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[AuthorizationEntryAttributes], jsii.get(self, "attributes"))


@jsii.implements(IAuthorizationPluginMap)
class AuthorizationMap(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AuthorizationMap",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        authorization_entries: typing.Optional[typing.Sequence[IAuthorizationMapAuthorizationEntry]] = None,
        default_entry: typing.Optional[IAuthorizationMapDefaultEntry] = None,
        temp_destination_authorization_entry: typing.Optional["TempDestinationAuthorizationEntry"] = None,
    ) -> None:
        '''
        :param authorization_entries: 
        :param default_entry: 
        :param temp_destination_authorization_entry: 

        :stability: experimental
        '''
        elements = AuthorizationMapElements(
            authorization_entries=authorization_entries,
            default_entry=default_entry,
            temp_destination_authorization_entry=temp_destination_authorization_entry,
        )

        jsii.create(self.__class__, self, [elements])

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[AuthorizationMapElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[AuthorizationMapElements], jsii.get(self, "elements"))


@jsii.implements(IBrokerPlugin)
class AuthorizationPlugin(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.AuthorizationPlugin",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        authorization_map: typing.Optional[IAuthorizationPluginMap] = None,
    ) -> None:
        '''
        :param authorization_map: 

        :stability: experimental
        '''
        elements = AuthorizationPluginElements(authorization_map=authorization_map)

        jsii.create(self.__class__, self, [elements])

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[AuthorizationPluginElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[AuthorizationPluginElements], jsii.get(self, "elements"))


class Broker(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.Broker",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        attributes: typing.Optional[typing.Union[BrokerAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        *,
        destination_interceptors: typing.Optional[typing.Sequence[IBrokerDestinationInterceptor]] = None,
        destination_policy: typing.Optional["PolicyMap"] = None,
        destinations: typing.Optional[typing.Sequence[IBrokerDestination]] = None,
        network_connectors: typing.Optional[typing.Sequence["NetworkConnector"]] = None,
        persistence_adapter: typing.Optional["KahaDB"] = None,
        plugins: typing.Optional[typing.Sequence[IBrokerPlugin]] = None,
        system_usage: typing.Optional["SystemUsage"] = None,
        transport_connectors: typing.Optional[typing.Sequence["TransportConnector"]] = None,
    ) -> None:
        '''
        :param attributes: -
        :param destination_interceptors: 
        :param destination_policy: 
        :param destinations: 
        :param network_connectors: 
        :param persistence_adapter: 
        :param plugins: 
        :param system_usage: 
        :param transport_connectors: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b86807a21059632c4ecda964b38deac635d4925a9efc4d3abec2d74eb47f6049)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        elements = BrokerElements(
            destination_interceptors=destination_interceptors,
            destination_policy=destination_policy,
            destinations=destinations,
            network_connectors=network_connectors,
            persistence_adapter=persistence_adapter,
            plugins=plugins,
            system_usage=system_usage,
            transport_connectors=transport_connectors,
        )

        jsii.create(self.__class__, self, [attributes, elements])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[BrokerAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[BrokerAttributes], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[BrokerElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[BrokerElements], jsii.get(self, "elements"))


@jsii.implements(IAuthorizationPluginMap)
class CachedLDAPAuthorizationMap(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CachedLDAPAuthorizationMap",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        legacy_group_mapping: typing.Optional[builtins.bool] = None,
        queue_search_base: typing.Optional[builtins.str] = None,
        refresh_interval: typing.Optional[jsii.Number] = None,
        temp_search_base: typing.Optional[builtins.str] = None,
        topic_search_base: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param legacy_group_mapping: 
        :param queue_search_base: 
        :param refresh_interval: 
        :param temp_search_base: 
        :param topic_search_base: 

        :stability: experimental
        '''
        attributes = CachedLDAPAuthorizationMapAttributes(
            legacy_group_mapping=legacy_group_mapping,
            queue_search_base=queue_search_base,
            refresh_interval=refresh_interval,
            temp_search_base=temp_search_base,
            topic_search_base=topic_search_base,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[CachedLDAPAuthorizationMapAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[CachedLDAPAuthorizationMapAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryMessageGroupMapFactory)
class CachedMessageGroupMapFactory(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CachedMessageGroupMapFactory",
):
    '''
    :stability: experimental
    '''

    def __init__(self, *, cache_size: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param cache_size: 

        :stability: experimental
        '''
        attributes = CachedMessageGroupMapFactoryAttributes(cache_size=cache_size)

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[CachedMessageGroupMapFactoryAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[CachedMessageGroupMapFactoryAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryDispatchPolicy)
class ClientIdFilterDispatchPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ClientIdFilterDispatchPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        ptp_client_id: typing.Optional[builtins.str] = None,
        ptp_suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ptp_client_id: 
        :param ptp_suffix: 

        :stability: experimental
        '''
        attributes = ClientIdFilterDispatchPolicyAttributes(
            ptp_client_id=ptp_client_id, ptp_suffix=ptp_suffix
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[ClientIdFilterDispatchPolicyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[ClientIdFilterDispatchPolicyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IVirtualDestinationInterceptorVirtualDestination)
class CompositeQueue(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CompositeQueue",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        attributes: typing.Optional[typing.Union[CompositeQueueAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        *,
        forward_to: typing.Optional[typing.Sequence[ICompositeQueueForwardTo]] = None,
    ) -> None:
        '''
        :param attributes: -
        :param forward_to: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38d361ae6f5af7a0fa988e81490664c79fe9c06331383ebe19dd631e901d6133)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        elements = CompositeQueueElements(forward_to=forward_to)

        jsii.create(self.__class__, self, [attributes, elements])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[CompositeQueueAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[CompositeQueueAttributes], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[CompositeQueueElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[CompositeQueueElements], jsii.get(self, "elements"))


@jsii.implements(IVirtualDestinationInterceptorVirtualDestination)
class CompositeTopic(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.CompositeTopic",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        attributes: typing.Optional[typing.Union[CompositeTopicAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        *,
        forward_to: typing.Optional[typing.Sequence[ICompositeTopicForwardTo]] = None,
    ) -> None:
        '''
        :param attributes: -
        :param forward_to: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__533ac9d1b4aa6b766e74ceb0cbd1e24b2574bd8c5cd63b4c3743697abb5c842b)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        elements = CompositeTopicElements(forward_to=forward_to)

        jsii.create(self.__class__, self, [attributes, elements])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[CompositeTopicAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[CompositeTopicAttributes], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[CompositeTopicElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[CompositeTopicElements], jsii.get(self, "elements"))


class ConditionalNetworkBridgeFilterFactory(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ConditionalNetworkBridgeFilterFactory",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        rate_duration: typing.Optional[jsii.Number] = None,
        rate_limit: typing.Optional[jsii.Number] = None,
        replay_delay: typing.Optional[jsii.Number] = None,
        replay_when_no_consumers: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param rate_duration: 
        :param rate_limit: 
        :param replay_delay: 
        :param replay_when_no_consumers: 

        :stability: experimental
        '''
        attributes = ConditionalNetworkBridgeFilterFactoryAttributes(
            rate_duration=rate_duration,
            rate_limit=rate_limit,
            replay_delay=replay_delay,
            replay_when_no_consumers=replay_when_no_consumers,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[ConditionalNetworkBridgeFilterFactoryAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[ConditionalNetworkBridgeFilterFactoryAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryPendingMessageLimitStrategy)
class ConstantPendingMessageLimitStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ConstantPendingMessageLimitStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(self, *, limit: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param limit: 

        :stability: experimental
        '''
        attributes = ConstantPendingMessageLimitStrategyAttributes(limit=limit)

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[ConstantPendingMessageLimitStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[ConstantPendingMessageLimitStrategyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryDeadLetterStrategy)
class Discarding(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.Discarding",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[builtins.str] = None,
        enable_audit: typing.Optional[builtins.bool] = None,
        expiration: typing.Optional[jsii.Number] = None,
        max_audit_depth: typing.Optional[jsii.Number] = None,
        max_producers_to_audit: typing.Optional[jsii.Number] = None,
        process_expired: typing.Optional[builtins.bool] = None,
        process_non_persistent: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param dead_letter_queue: 
        :param enable_audit: 
        :param expiration: 
        :param max_audit_depth: 
        :param max_producers_to_audit: 
        :param process_expired: 
        :param process_non_persistent: 

        :stability: experimental
        '''
        attributes = DiscardingAttributes(
            dead_letter_queue=dead_letter_queue,
            enable_audit=enable_audit,
            expiration=expiration,
            max_audit_depth=max_audit_depth,
            max_producers_to_audit=max_producers_to_audit,
            process_expired=process_expired,
            process_non_persistent=process_non_persistent,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[DiscardingAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[DiscardingAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerPlugin)
class DiscardingDLQBrokerPlugin(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.DiscardingDLQBrokerPlugin",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        drop_all: typing.Optional[builtins.bool] = None,
        drop_only: typing.Optional[builtins.str] = None,
        drop_temporary_queues: typing.Optional[builtins.bool] = None,
        drop_temporary_topics: typing.Optional[builtins.bool] = None,
        report_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param drop_all: 
        :param drop_only: 
        :param drop_temporary_queues: 
        :param drop_temporary_topics: 
        :param report_interval: 

        :stability: experimental
        '''
        attributes = DiscardingDLQBrokerPluginAttributes(
            drop_all=drop_all,
            drop_only=drop_only,
            drop_temporary_queues=drop_temporary_queues,
            drop_temporary_topics=drop_temporary_topics,
            report_interval=report_interval,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[DiscardingDLQBrokerPluginAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[DiscardingDLQBrokerPluginAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryPendingSubscriberPolicy)
class FileCursor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FileCursor",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryPendingDurableSubscriberPolicy)
class FileDurableSubscriberCursor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FileDurableSubscriberCursor",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryPendingQueuePolicy)
class FileQueueCursor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FileQueueCursor",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(ICompositeQueueForwardTo, ICompositeTopicForwardTo, INetworkConnectorDurableDestination, INetworkConnectorDynamicallyIncludedDestination, INetworkConnectorExcludedDestination, INetworkConnectorStaticallyIncludedDestination)
class FilteredDestination(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FilteredDestination",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        queue: typing.Optional[builtins.str] = None,
        selector: typing.Optional[builtins.str] = None,
        topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param queue: 
        :param selector: 
        :param topic: 

        :stability: experimental
        '''
        attributes = FilteredDestinationAttributes(
            queue=queue, selector=selector, topic=topic
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[FilteredDestinationAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[FilteredDestinationAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntrySubscriptionRecoveryPolicy, IRetainedMessageSubscriptionRecoveryPolicyWrapped)
class FixedCountSubscriptionRecoveryPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FixedCountSubscriptionRecoveryPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self, *, maximum_size: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param maximum_size: 

        :stability: experimental
        '''
        attributes = FixedCountSubscriptionRecoveryPolicyAttributes(
            maximum_size=maximum_size
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[FixedCountSubscriptionRecoveryPolicyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[FixedCountSubscriptionRecoveryPolicyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntrySubscriptionRecoveryPolicy, IRetainedMessageSubscriptionRecoveryPolicyWrapped)
class FixedSizedSubscriptionRecoveryPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.FixedSizedSubscriptionRecoveryPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        maximum_size: typing.Optional[jsii.Number] = None,
        use_shared_buffer: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param maximum_size: 
        :param use_shared_buffer: 

        :stability: experimental
        '''
        attributes = FixedSizedSubscriptionRecoveryPolicyAttributes(
            maximum_size=maximum_size, use_shared_buffer=use_shared_buffer
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[FixedSizedSubscriptionRecoveryPolicyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[FixedSizedSubscriptionRecoveryPolicyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerPlugin)
class ForcePersistencyModeBrokerPlugin(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.ForcePersistencyModeBrokerPlugin",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        persistence_flag: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param persistence_flag: 

        :stability: experimental
        '''
        attributes = ForcePersistencyModeBrokerPluginAttributes(
            persistence_flag=persistence_flag
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[ForcePersistencyModeBrokerPluginAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[ForcePersistencyModeBrokerPluginAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryDeadLetterStrategy)
class IndividualDeadLetterStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.IndividualDeadLetterStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        destination_per_durable_subscriber: typing.Optional[builtins.bool] = None,
        enable_audit: typing.Optional[builtins.bool] = None,
        expiration: typing.Optional[jsii.Number] = None,
        max_audit_depth: typing.Optional[jsii.Number] = None,
        max_producers_to_audit: typing.Optional[jsii.Number] = None,
        process_expired: typing.Optional[builtins.bool] = None,
        process_non_persistent: typing.Optional[builtins.bool] = None,
        queue_prefix: typing.Optional[builtins.str] = None,
        queue_suffix: typing.Optional[builtins.str] = None,
        topic_prefix: typing.Optional[builtins.str] = None,
        topic_suffix: typing.Optional[builtins.str] = None,
        use_queue_for_queue_messages: typing.Optional[builtins.bool] = None,
        use_queue_for_topic_messages: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param destination_per_durable_subscriber: 
        :param enable_audit: 
        :param expiration: 
        :param max_audit_depth: 
        :param max_producers_to_audit: 
        :param process_expired: 
        :param process_non_persistent: 
        :param queue_prefix: 
        :param queue_suffix: 
        :param topic_prefix: 
        :param topic_suffix: 
        :param use_queue_for_queue_messages: 
        :param use_queue_for_topic_messages: 

        :stability: experimental
        '''
        attributes = IndividualDeadLetterStrategyAttributes(
            destination_per_durable_subscriber=destination_per_durable_subscriber,
            enable_audit=enable_audit,
            expiration=expiration,
            max_audit_depth=max_audit_depth,
            max_producers_to_audit=max_producers_to_audit,
            process_expired=process_expired,
            process_non_persistent=process_non_persistent,
            queue_prefix=queue_prefix,
            queue_suffix=queue_suffix,
            topic_prefix=topic_prefix,
            topic_suffix=topic_suffix,
            use_queue_for_queue_messages=use_queue_for_queue_messages,
            use_queue_for_topic_messages=use_queue_for_topic_messages,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[IndividualDeadLetterStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[IndividualDeadLetterStrategyAttributes], jsii.get(self, "attributes"))


class KahaDB(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.KahaDB",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        checkpoint_interval: typing.Optional[jsii.Number] = None,
        concurrent_store_and_dispatch_queues: typing.Optional[builtins.bool] = None,
        index_write_batch_size: typing.Optional[jsii.Number] = None,
        journal_disk_sync_interval: typing.Optional[jsii.Number] = None,
        journal_disk_sync_strategy: typing.Optional[JournalDiskSyncStrategy] = None,
        preallocation_strategy: typing.Optional[PreallocationStrategy] = None,
    ) -> None:
        '''
        :param checkpoint_interval: 
        :param concurrent_store_and_dispatch_queues: 
        :param index_write_batch_size: 
        :param journal_disk_sync_interval: 
        :param journal_disk_sync_strategy: 
        :param preallocation_strategy: 

        :stability: experimental
        '''
        attributes = KahaDBAttributes(
            checkpoint_interval=checkpoint_interval,
            concurrent_store_and_dispatch_queues=concurrent_store_and_dispatch_queues,
            index_write_batch_size=index_write_batch_size,
            journal_disk_sync_interval=journal_disk_sync_interval,
            journal_disk_sync_strategy=journal_disk_sync_strategy,
            preallocation_strategy=preallocation_strategy,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[KahaDBAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[KahaDBAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntrySubscriptionRecoveryPolicy, IRetainedMessageSubscriptionRecoveryPolicyWrapped)
class LastImageSubscriptionRecoveryPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.LastImageSubscriptionRecoveryPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


class MemoryUsage(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.MemoryUsage",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        percent_of_jvm_heap: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param percent_of_jvm_heap: 

        :stability: experimental
        '''
        attributes = MemoryUsageAttributes(percent_of_jvm_heap=percent_of_jvm_heap)

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[MemoryUsageAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[MemoryUsageAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryMessageGroupMapFactory)
class MessageGroupHashBucketFactory(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.MessageGroupHashBucketFactory",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        bucket_count: typing.Optional[jsii.Number] = None,
        cache_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param bucket_count: 
        :param cache_size: 

        :stability: experimental
        '''
        attributes = MessageGroupHashBucketFactoryAttributes(
            bucket_count=bucket_count, cache_size=cache_size
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[MessageGroupHashBucketFactoryAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[MessageGroupHashBucketFactoryAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerDestinationInterceptor)
class MirroredQueue(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.MirroredQueue",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        copy_message: typing.Optional[builtins.bool] = None,
        postfix: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param copy_message: 
        :param postfix: 
        :param prefix: 

        :stability: experimental
        '''
        attributes = MirroredQueueAttributes(
            copy_message=copy_message, postfix=postfix, prefix=prefix
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[MirroredQueueAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[MirroredQueueAttributes], jsii.get(self, "attributes"))


class NetworkConnector(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.NetworkConnector",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        attributes: typing.Optional[typing.Union[NetworkConnectorAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        *,
        durable_destinations: typing.Optional[typing.Sequence[INetworkConnectorDurableDestination]] = None,
        dynamically_included_destinations: typing.Optional[typing.Sequence[INetworkConnectorDynamicallyIncludedDestination]] = None,
        excluded_destinations: typing.Optional[typing.Sequence[INetworkConnectorExcludedDestination]] = None,
        statically_included_destinations: typing.Optional[typing.Sequence[INetworkConnectorStaticallyIncludedDestination]] = None,
    ) -> None:
        '''
        :param attributes: -
        :param durable_destinations: 
        :param dynamically_included_destinations: 
        :param excluded_destinations: 
        :param statically_included_destinations: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c8209e37f7ad27ae3038be0302d136b5e39e2cc94a82b2f86589e72832bdf60)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        elements = NetworkConnectorElements(
            durable_destinations=durable_destinations,
            dynamically_included_destinations=dynamically_included_destinations,
            excluded_destinations=excluded_destinations,
            statically_included_destinations=statically_included_destinations,
        )

        jsii.create(self.__class__, self, [attributes, elements])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[NetworkConnectorAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[NetworkConnectorAttributes], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[NetworkConnectorElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[NetworkConnectorElements], jsii.get(self, "elements"))


@jsii.implements(IPolicyEntrySubscriptionRecoveryPolicy, IRetainedMessageSubscriptionRecoveryPolicyWrapped)
class NoSubscriptionRecoveryPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.NoSubscriptionRecoveryPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryMessageEvictionStrategy)
class OldestMessageEvictionStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.OldestMessageEvictionStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evict_expired_messages_high_watermark: 

        :stability: experimental
        '''
        attributes = OldestMessageEvictionStrategyAttributes(
            evict_expired_messages_high_watermark=evict_expired_messages_high_watermark
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[OldestMessageEvictionStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[OldestMessageEvictionStrategyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryMessageEvictionStrategy)
class OldestMessageWithLowestPriorityEvictionStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.OldestMessageWithLowestPriorityEvictionStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param evict_expired_messages_high_watermark: 

        :stability: experimental
        '''
        attributes = OldestMessageWithLowestPriorityEvictionStrategyAttributes(
            evict_expired_messages_high_watermark=evict_expired_messages_high_watermark
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[OldestMessageWithLowestPriorityEvictionStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[OldestMessageWithLowestPriorityEvictionStrategyAttributes], jsii.get(self, "attributes"))


class PolicyEntry(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PolicyEntry",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        attributes: typing.Optional[typing.Union[PolicyEntryAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        *,
        dead_letter_strategy: typing.Optional[IPolicyEntryDeadLetterStrategy] = None,
        destination: typing.Optional[IPolicyEntryDestination] = None,
        dispatch_policy: typing.Optional[IPolicyEntryDispatchPolicy] = None,
        message_eviction_strategy: typing.Optional[IPolicyEntryMessageEvictionStrategy] = None,
        message_group_map_factory: typing.Optional[IPolicyEntryMessageGroupMapFactory] = None,
        network_bridge_filter_factory: typing.Optional[ConditionalNetworkBridgeFilterFactory] = None,
        pending_durable_subscriber_policy: typing.Optional[IPolicyEntryPendingDurableSubscriberPolicy] = None,
        pending_message_limit_strategy: typing.Optional[IPolicyEntryPendingMessageLimitStrategy] = None,
        pending_queue_policy: typing.Optional[IPolicyEntryPendingQueuePolicy] = None,
        pending_subscriber_policy: typing.Optional[IPolicyEntryPendingSubscriberPolicy] = None,
        slow_consumer_strategy: typing.Optional[IPolicyEntrySlowConsumerStrategy] = None,
        subscription_recovery_policy: typing.Optional[IPolicyEntrySubscriptionRecoveryPolicy] = None,
    ) -> None:
        '''
        :param attributes: -
        :param dead_letter_strategy: 
        :param destination: 
        :param dispatch_policy: 
        :param message_eviction_strategy: 
        :param message_group_map_factory: 
        :param network_bridge_filter_factory: 
        :param pending_durable_subscriber_policy: 
        :param pending_message_limit_strategy: 
        :param pending_queue_policy: 
        :param pending_subscriber_policy: 
        :param slow_consumer_strategy: 
        :param subscription_recovery_policy: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974fb4dd1e99e08ccb1cb147c121753b9ff7c54f03b0a10b55e053414e5d72dc)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        elements = PolicyEntryElements(
            dead_letter_strategy=dead_letter_strategy,
            destination=destination,
            dispatch_policy=dispatch_policy,
            message_eviction_strategy=message_eviction_strategy,
            message_group_map_factory=message_group_map_factory,
            network_bridge_filter_factory=network_bridge_filter_factory,
            pending_durable_subscriber_policy=pending_durable_subscriber_policy,
            pending_message_limit_strategy=pending_message_limit_strategy,
            pending_queue_policy=pending_queue_policy,
            pending_subscriber_policy=pending_subscriber_policy,
            slow_consumer_strategy=slow_consumer_strategy,
            subscription_recovery_policy=subscription_recovery_policy,
        )

        jsii.create(self.__class__, self, [attributes, elements])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[PolicyEntryAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[PolicyEntryAttributes], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[PolicyEntryElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[PolicyEntryElements], jsii.get(self, "elements"))


class PolicyMap(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PolicyMap",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        default_entry: typing.Optional[PolicyEntry] = None,
        policy_entries: typing.Optional[typing.Sequence[PolicyEntry]] = None,
    ) -> None:
        '''
        :param default_entry: 
        :param policy_entries: 

        :stability: experimental
        '''
        elements = PolicyMapElements(
            default_entry=default_entry, policy_entries=policy_entries
        )

        jsii.create(self.__class__, self, [elements])

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[PolicyMapElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[PolicyMapElements], jsii.get(self, "elements"))


@jsii.implements(IPolicyEntryPendingMessageLimitStrategy)
class PrefetchRatePendingMessageLimitStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PrefetchRatePendingMessageLimitStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(self, *, multiplier: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param multiplier: 

        :stability: experimental
        '''
        attributes = PrefetchRatePendingMessageLimitStrategyAttributes(
            multiplier=multiplier
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[PrefetchRatePendingMessageLimitStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[PrefetchRatePendingMessageLimitStrategyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryDispatchPolicy)
class PriorityDispatchPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PriorityDispatchPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryDispatchPolicy)
class PriorityNetworkDispatchPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.PriorityNetworkDispatchPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntrySubscriptionRecoveryPolicy, IRetainedMessageSubscriptionRecoveryPolicyWrapped)
class QueryBasedSubscriptionRecoveryPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.QueryBasedSubscriptionRecoveryPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self, *, query: typing.Optional[builtins.str] = None) -> None:
        '''
        :param query: 

        :stability: experimental
        '''
        attributes = QueryBasedSubscriptionRecoveryPolicyAttributes(query=query)

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[QueryBasedSubscriptionRecoveryPolicyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[QueryBasedSubscriptionRecoveryPolicyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerDestination, ICompositeQueueForwardTo, ICompositeTopicForwardTo, INetworkConnectorDurableDestination, INetworkConnectorDynamicallyIncludedDestination, INetworkConnectorExcludedDestination, INetworkConnectorStaticallyIncludedDestination, IPolicyEntryDestination, ISharedDeadLetterStrategyDeadLetterQueue)
class Queue(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.Queue",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        dlq: typing.Optional[builtins.bool] = None,
        physical_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dlq: 
        :param physical_name: 

        :stability: experimental
        '''
        attributes = QueueAttributes(dlq=dlq, physical_name=physical_name)

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[QueueAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[QueueAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerPlugin)
class RedeliveryPlugin(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RedeliveryPlugin",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        attributes: typing.Optional[typing.Union[RedeliveryPluginAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        *,
        redelivery_policy_map: typing.Optional["RedeliveryPolicyMap"] = None,
    ) -> None:
        '''
        :param attributes: -
        :param redelivery_policy_map: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09aa41f17317e87dd1259cff1522c4036fa95063d6b25f969749b491e7490e79)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        elements = RedeliveryPluginElements(
            redelivery_policy_map=redelivery_policy_map
        )

        jsii.create(self.__class__, self, [attributes, elements])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[RedeliveryPluginAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[RedeliveryPluginAttributes], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[RedeliveryPluginElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[RedeliveryPluginElements], jsii.get(self, "elements"))


class RedeliveryPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RedeliveryPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        back_off_multiplier: typing.Optional[jsii.Number] = None,
        collision_avoidance_percent: typing.Optional[jsii.Number] = None,
        initial_redelivery_delay: typing.Optional[jsii.Number] = None,
        maximum_redeliveries: typing.Optional[jsii.Number] = None,
        maximum_redelivery_delay: typing.Optional[jsii.Number] = None,
        pre_dispatch_check: typing.Optional[builtins.bool] = None,
        queue: typing.Optional[builtins.str] = None,
        redelivery_delay: typing.Optional[jsii.Number] = None,
        temp_queue: typing.Optional[builtins.bool] = None,
        temp_topic: typing.Optional[builtins.bool] = None,
        topic: typing.Optional[builtins.str] = None,
        use_collision_avoidance: typing.Optional[builtins.bool] = None,
        use_exponential_back_off: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param back_off_multiplier: 
        :param collision_avoidance_percent: 
        :param initial_redelivery_delay: 
        :param maximum_redeliveries: 
        :param maximum_redelivery_delay: 
        :param pre_dispatch_check: 
        :param queue: 
        :param redelivery_delay: 
        :param temp_queue: 
        :param temp_topic: 
        :param topic: 
        :param use_collision_avoidance: 
        :param use_exponential_back_off: 

        :stability: experimental
        '''
        attributes = RedeliveryPolicyAttributes(
            back_off_multiplier=back_off_multiplier,
            collision_avoidance_percent=collision_avoidance_percent,
            initial_redelivery_delay=initial_redelivery_delay,
            maximum_redeliveries=maximum_redeliveries,
            maximum_redelivery_delay=maximum_redelivery_delay,
            pre_dispatch_check=pre_dispatch_check,
            queue=queue,
            redelivery_delay=redelivery_delay,
            temp_queue=temp_queue,
            temp_topic=temp_topic,
            topic=topic,
            use_collision_avoidance=use_collision_avoidance,
            use_exponential_back_off=use_exponential_back_off,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[RedeliveryPolicyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[RedeliveryPolicyAttributes], jsii.get(self, "attributes"))


class RedeliveryPolicyMap(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RedeliveryPolicyMap",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        default_entry: typing.Optional[RedeliveryPolicy] = None,
        redelivery_policy_entries: typing.Optional[typing.Sequence[RedeliveryPolicy]] = None,
    ) -> None:
        '''
        :param default_entry: 
        :param redelivery_policy_entries: 

        :stability: experimental
        '''
        elements = RedeliveryPolicyMapElements(
            default_entry=default_entry,
            redelivery_policy_entries=redelivery_policy_entries,
        )

        jsii.create(self.__class__, self, [elements])

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[RedeliveryPolicyMapElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[RedeliveryPolicyMapElements], jsii.get(self, "elements"))


@jsii.implements(IPolicyEntrySubscriptionRecoveryPolicy, IRetainedMessageSubscriptionRecoveryPolicyWrapped)
class RetainedMessageSubscriptionRecoveryPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RetainedMessageSubscriptionRecoveryPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        wrapped: typing.Optional[IRetainedMessageSubscriptionRecoveryPolicyWrapped] = None,
    ) -> None:
        '''
        :param wrapped: 

        :stability: experimental
        '''
        elements = RetainedMessageSubscriptionRecoveryPolicyElements(wrapped=wrapped)

        jsii.create(self.__class__, self, [elements])

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(
        self,
    ) -> typing.Optional[RetainedMessageSubscriptionRecoveryPolicyElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[RetainedMessageSubscriptionRecoveryPolicyElements], jsii.get(self, "elements"))


@jsii.implements(IPolicyEntryDispatchPolicy)
class RoundRobinDispatchPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.RoundRobinDispatchPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryDeadLetterStrategy)
class SharedDeadLetterStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.SharedDeadLetterStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        attributes: typing.Optional[typing.Union[SharedDeadLetterStrategyAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        *,
        dead_letter_queue: typing.Optional[ISharedDeadLetterStrategyDeadLetterQueue] = None,
    ) -> None:
        '''
        :param attributes: -
        :param dead_letter_queue: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c961dc576afdf1ca90429c3cb3a32260094088dd8a9b977c7c2ac5e2525d92d)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        elements = SharedDeadLetterStrategyElements(
            dead_letter_queue=dead_letter_queue
        )

        jsii.create(self.__class__, self, [attributes, elements])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[SharedDeadLetterStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[SharedDeadLetterStrategyAttributes], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[SharedDeadLetterStrategyElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[SharedDeadLetterStrategyElements], jsii.get(self, "elements"))


@jsii.implements(IPolicyEntryDispatchPolicy)
class SimpleDispatchPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.SimpleDispatchPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryMessageGroupMapFactory)
class SimpleMessageGroupMapFactory(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.SimpleMessageGroupMapFactory",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IBrokerPlugin)
class StatisticsBrokerPlugin(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.StatisticsBrokerPlugin",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryPendingQueuePolicy)
class StoreCursor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.StoreCursor",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryPendingDurableSubscriberPolicy)
class StoreDurableSubscriberCursor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.StoreDurableSubscriberCursor",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        immediate_priority_dispatch: typing.Optional[builtins.bool] = None,
        use_cache: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param immediate_priority_dispatch: 
        :param use_cache: 

        :stability: experimental
        '''
        attributes = StoreDurableSubscriberCursorAttributes(
            immediate_priority_dispatch=immediate_priority_dispatch,
            use_cache=use_cache,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[StoreDurableSubscriberCursorAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[StoreDurableSubscriberCursorAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryDispatchPolicy)
class StrictOrderDispatchPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.StrictOrderDispatchPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


class SystemUsage(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.SystemUsage",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        attributes: typing.Optional[typing.Union[SystemUsageAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        *,
        memory_usage: typing.Optional[MemoryUsage] = None,
    ) -> None:
        '''
        :param attributes: -
        :param memory_usage: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba34c1586ba6070c23266ec12af9620b7284fdae61c7df8795e6a4d53a29d33)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        elements = SystemUsageElements(memory_usage=memory_usage)

        jsii.create(self.__class__, self, [attributes, elements])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[SystemUsageAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[SystemUsageAttributes], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[SystemUsageElements]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[SystemUsageElements], jsii.get(self, "elements"))


@jsii.implements(IAuthorizationMapAuthorizationEntry, IAuthorizationMapDefaultEntry)
class TempDestinationAuthorizationEntry(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TempDestinationAuthorizationEntry",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        admin: typing.Optional[builtins.str] = None,
        queue: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        temp_queue: typing.Optional[builtins.bool] = None,
        temp_topic: typing.Optional[builtins.bool] = None,
        topic: typing.Optional[builtins.str] = None,
        write: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin: 
        :param queue: 
        :param read: 
        :param temp_queue: 
        :param temp_topic: 
        :param topic: 
        :param write: 

        :stability: experimental
        '''
        attributes = TempDestinationAuthorizationEntryAttributes(
            admin=admin,
            queue=queue,
            read=read,
            temp_queue=temp_queue,
            temp_topic=temp_topic,
            topic=topic,
            write=write,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[TempDestinationAuthorizationEntryAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TempDestinationAuthorizationEntryAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerDestination, ICompositeQueueForwardTo, ICompositeTopicForwardTo, INetworkConnectorDurableDestination, INetworkConnectorDynamicallyIncludedDestination, INetworkConnectorExcludedDestination, INetworkConnectorStaticallyIncludedDestination, IPolicyEntryDestination, ISharedDeadLetterStrategyDeadLetterQueue)
class TempQueue(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TempQueue",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        dlq: typing.Optional[builtins.bool] = None,
        physical_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dlq: 
        :param physical_name: 

        :stability: experimental
        '''
        attributes = TempQueueAttributes(dlq=dlq, physical_name=physical_name)

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[TempQueueAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TempQueueAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerDestination, ICompositeQueueForwardTo, ICompositeTopicForwardTo, INetworkConnectorDurableDestination, INetworkConnectorDynamicallyIncludedDestination, INetworkConnectorExcludedDestination, INetworkConnectorStaticallyIncludedDestination, IPolicyEntryDestination, ISharedDeadLetterStrategyDeadLetterQueue)
class TempTopic(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TempTopic",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        dlq: typing.Optional[builtins.bool] = None,
        physical_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dlq: 
        :param physical_name: 

        :stability: experimental
        '''
        attributes = TempTopicAttributes(dlq=dlq, physical_name=physical_name)

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[TempTopicAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TempTopicAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerPlugin)
class TimeStampingBrokerPlugin(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TimeStampingBrokerPlugin",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        future_only: typing.Optional[builtins.bool] = None,
        process_network_messages: typing.Optional[builtins.bool] = None,
        ttl_ceiling: typing.Optional[jsii.Number] = None,
        zero_expiration_override: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param future_only: 
        :param process_network_messages: 
        :param ttl_ceiling: 
        :param zero_expiration_override: 

        :stability: experimental
        '''
        attributes = TimeStampingBrokerPluginAttributes(
            future_only=future_only,
            process_network_messages=process_network_messages,
            ttl_ceiling=ttl_ceiling,
            zero_expiration_override=zero_expiration_override,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[TimeStampingBrokerPluginAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TimeStampingBrokerPluginAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntrySubscriptionRecoveryPolicy, IRetainedMessageSubscriptionRecoveryPolicyWrapped)
class TimedSubscriptionRecoveryPolicy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TimedSubscriptionRecoveryPolicy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        recover_duration: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param recover_duration: 

        :stability: experimental
        '''
        attributes = TimedSubscriptionRecoveryPolicyAttributes(
            recover_duration=recover_duration
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[TimedSubscriptionRecoveryPolicyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TimedSubscriptionRecoveryPolicyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerDestination, ICompositeQueueForwardTo, ICompositeTopicForwardTo, INetworkConnectorDurableDestination, INetworkConnectorDynamicallyIncludedDestination, INetworkConnectorExcludedDestination, INetworkConnectorStaticallyIncludedDestination, IPolicyEntryDestination, ISharedDeadLetterStrategyDeadLetterQueue)
class Topic(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.Topic",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        dlq: typing.Optional[builtins.bool] = None,
        physical_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dlq: 
        :param physical_name: 

        :stability: experimental
        '''
        attributes = TopicAttributes(dlq=dlq, physical_name=physical_name)

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[TopicAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TopicAttributes], jsii.get(self, "attributes"))


class TransportConnector(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.TransportConnector",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        name: typing.Optional[Protocol] = None,
        rebalance_cluster_clients: typing.Optional[builtins.bool] = None,
        update_cluster_clients: typing.Optional[builtins.bool] = None,
        update_cluster_clients_on_remove: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param name: 
        :param rebalance_cluster_clients: 
        :param update_cluster_clients: 
        :param update_cluster_clients_on_remove: 

        :stability: experimental
        '''
        attributes = TransportConnectorAttributes(
            name=name,
            rebalance_cluster_clients=rebalance_cluster_clients,
            update_cluster_clients=update_cluster_clients,
            update_cluster_clients_on_remove=update_cluster_clients_on_remove,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[TransportConnectorAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[TransportConnectorAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryMessageEvictionStrategy)
class UniquePropertyMessageEvictionStrategy(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.UniquePropertyMessageEvictionStrategy",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
        property_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param evict_expired_messages_high_watermark: 
        :param property_name: 

        :stability: experimental
        '''
        attributes = UniquePropertyMessageEvictionStrategyAttributes(
            evict_expired_messages_high_watermark=evict_expired_messages_high_watermark,
            property_name=property_name,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[UniquePropertyMessageEvictionStrategyAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[UniquePropertyMessageEvictionStrategyAttributes], jsii.get(self, "attributes"))


@jsii.implements(IBrokerDestinationInterceptor)
class VirtualDestinationInterceptor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.VirtualDestinationInterceptor",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        virtual_destinations: typing.Sequence[IVirtualDestinationInterceptorVirtualDestination],
    ) -> None:
        '''
        :param virtual_destinations: 

        :stability: experimental
        '''
        elements = VirtualDestinationInterceptorElements(
            virtual_destinations=virtual_destinations
        )

        jsii.create(self.__class__, self, [elements])

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> VirtualDestinationInterceptorElements:
        '''
        :stability: experimental
        '''
        return typing.cast(VirtualDestinationInterceptorElements, jsii.get(self, "elements"))


@jsii.implements(IVirtualDestinationInterceptorVirtualDestination)
class VirtualTopic(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.VirtualTopic",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        *,
        concurrent_send: typing.Optional[builtins.bool] = None,
        local: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        postfix: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        selector_aware: typing.Optional[builtins.bool] = None,
        transacted_send: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param concurrent_send: 
        :param local: 
        :param name: 
        :param postfix: 
        :param prefix: 
        :param selector_aware: 
        :param transacted_send: 

        :stability: experimental
        '''
        attributes = VirtualTopicAttributes(
            concurrent_send=concurrent_send,
            local=local,
            name=name,
            postfix=postfix,
            prefix=prefix,
            selector_aware=selector_aware,
            transacted_send=transacted_send,
        )

        jsii.create(self.__class__, self, [attributes])

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[VirtualTopicAttributes]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[VirtualTopicAttributes], jsii.get(self, "attributes"))


@jsii.implements(IPolicyEntryPendingSubscriberPolicy)
class VmCursor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.VmCursor",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryPendingDurableSubscriberPolicy)
class VmDurableCursor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.VmDurableCursor",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


@jsii.implements(IPolicyEntryPendingQueuePolicy)
class VmQueueCursor(
    XmlNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-amazonmq-activemq-config-v5-15-16.VmQueueCursor",
):
    '''
    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])


__all__ = [
    "AbortSlowAckConsumerStrategy",
    "AbortSlowAckConsumerStrategyAttributes",
    "AbortSlowConsumerStrategy",
    "AbortSlowConsumerStrategyAttributes",
    "AuthorizationEntry",
    "AuthorizationEntryAttributes",
    "AuthorizationMap",
    "AuthorizationMapElements",
    "AuthorizationPlugin",
    "AuthorizationPluginElements",
    "Broker",
    "BrokerAttributes",
    "BrokerElements",
    "CachedLDAPAuthorizationMap",
    "CachedLDAPAuthorizationMapAttributes",
    "CachedMessageGroupMapFactory",
    "CachedMessageGroupMapFactoryAttributes",
    "ClientIdFilterDispatchPolicy",
    "ClientIdFilterDispatchPolicyAttributes",
    "CompositeQueue",
    "CompositeQueueAttributes",
    "CompositeQueueElements",
    "CompositeTopic",
    "CompositeTopicAttributes",
    "CompositeTopicElements",
    "ConditionalNetworkBridgeFilterFactory",
    "ConditionalNetworkBridgeFilterFactoryAttributes",
    "ConstantPendingMessageLimitStrategy",
    "ConstantPendingMessageLimitStrategyAttributes",
    "Discarding",
    "DiscardingAttributes",
    "DiscardingDLQBrokerPlugin",
    "DiscardingDLQBrokerPluginAttributes",
    "FileCursor",
    "FileDurableSubscriberCursor",
    "FileQueueCursor",
    "FilteredDestination",
    "FilteredDestinationAttributes",
    "FixedCountSubscriptionRecoveryPolicy",
    "FixedCountSubscriptionRecoveryPolicyAttributes",
    "FixedSizedSubscriptionRecoveryPolicy",
    "FixedSizedSubscriptionRecoveryPolicyAttributes",
    "ForcePersistencyModeBrokerPlugin",
    "ForcePersistencyModeBrokerPluginAttributes",
    "IAuthorizationMapAuthorizationEntry",
    "IAuthorizationMapDefaultEntry",
    "IAuthorizationPluginMap",
    "IBrokerDestination",
    "IBrokerDestinationInterceptor",
    "IBrokerPlugin",
    "ICompositeQueueForwardTo",
    "ICompositeTopicForwardTo",
    "INetworkConnectorDurableDestination",
    "INetworkConnectorDynamicallyIncludedDestination",
    "INetworkConnectorExcludedDestination",
    "INetworkConnectorStaticallyIncludedDestination",
    "IPolicyEntryDeadLetterStrategy",
    "IPolicyEntryDestination",
    "IPolicyEntryDispatchPolicy",
    "IPolicyEntryMessageEvictionStrategy",
    "IPolicyEntryMessageGroupMapFactory",
    "IPolicyEntryPendingDurableSubscriberPolicy",
    "IPolicyEntryPendingMessageLimitStrategy",
    "IPolicyEntryPendingQueuePolicy",
    "IPolicyEntryPendingSubscriberPolicy",
    "IPolicyEntrySlowConsumerStrategy",
    "IPolicyEntrySubscriptionRecoveryPolicy",
    "IRetainedMessageSubscriptionRecoveryPolicyWrapped",
    "ISharedDeadLetterStrategyDeadLetterQueue",
    "IVirtualDestinationInterceptorVirtualDestination",
    "IXmlNode",
    "IndividualDeadLetterStrategy",
    "IndividualDeadLetterStrategyAttributes",
    "JournalDiskSyncStrategy",
    "KahaDB",
    "KahaDBAttributes",
    "LastImageSubscriptionRecoveryPolicy",
    "MemoryUsage",
    "MemoryUsageAttributes",
    "MessageGroupHashBucketFactory",
    "MessageGroupHashBucketFactoryAttributes",
    "MirroredQueue",
    "MirroredQueueAttributes",
    "NetworkConnector",
    "NetworkConnectorAttributes",
    "NetworkConnectorElements",
    "NoSubscriptionRecoveryPolicy",
    "OldestMessageEvictionStrategy",
    "OldestMessageEvictionStrategyAttributes",
    "OldestMessageWithLowestPriorityEvictionStrategy",
    "OldestMessageWithLowestPriorityEvictionStrategyAttributes",
    "PolicyEntry",
    "PolicyEntryAttributes",
    "PolicyEntryElements",
    "PolicyMap",
    "PolicyMapElements",
    "PreallocationStrategy",
    "PrefetchRatePendingMessageLimitStrategy",
    "PrefetchRatePendingMessageLimitStrategyAttributes",
    "PriorityDispatchPolicy",
    "PriorityNetworkDispatchPolicy",
    "Protocol",
    "QueryBasedSubscriptionRecoveryPolicy",
    "QueryBasedSubscriptionRecoveryPolicyAttributes",
    "Queue",
    "QueueAttributes",
    "RedeliveryPlugin",
    "RedeliveryPluginAttributes",
    "RedeliveryPluginElements",
    "RedeliveryPolicy",
    "RedeliveryPolicyAttributes",
    "RedeliveryPolicyMap",
    "RedeliveryPolicyMapElements",
    "RetainedMessageSubscriptionRecoveryPolicy",
    "RetainedMessageSubscriptionRecoveryPolicyElements",
    "RoundRobinDispatchPolicy",
    "SharedDeadLetterStrategy",
    "SharedDeadLetterStrategyAttributes",
    "SharedDeadLetterStrategyElements",
    "SimpleDispatchPolicy",
    "SimpleMessageGroupMapFactory",
    "StatisticsBrokerPlugin",
    "StoreCursor",
    "StoreDurableSubscriberCursor",
    "StoreDurableSubscriberCursorAttributes",
    "StrictOrderDispatchPolicy",
    "SystemUsage",
    "SystemUsageAttributes",
    "SystemUsageElements",
    "TempDestinationAuthorizationEntry",
    "TempDestinationAuthorizationEntryAttributes",
    "TempQueue",
    "TempQueueAttributes",
    "TempTopic",
    "TempTopicAttributes",
    "TimeStampingBrokerPlugin",
    "TimeStampingBrokerPluginAttributes",
    "TimedSubscriptionRecoveryPolicy",
    "TimedSubscriptionRecoveryPolicyAttributes",
    "Topic",
    "TopicAttributes",
    "TransportConnector",
    "TransportConnectorAttributes",
    "UniquePropertyMessageEvictionStrategy",
    "UniquePropertyMessageEvictionStrategyAttributes",
    "VirtualDestinationInterceptor",
    "VirtualDestinationInterceptorElements",
    "VirtualTopic",
    "VirtualTopicAttributes",
    "VmCursor",
    "VmDurableCursor",
    "VmQueueCursor",
    "XmlNode",
    "XmlNodeProps",
]

publication.publish()

def _typecheckingstub__816d4e5bfd7583265c3326c7f9bdb14b5d2d4159647e3d0a64977d7ccdfb539d(
    *,
    abort_connection: typing.Optional[builtins.bool] = None,
    check_period: typing.Optional[jsii.Number] = None,
    ignore_idle_consumers: typing.Optional[builtins.bool] = None,
    ignore_network_consumers: typing.Optional[builtins.bool] = None,
    max_slow_count: typing.Optional[jsii.Number] = None,
    max_slow_duration: typing.Optional[jsii.Number] = None,
    max_time_since_last_ack: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3438312b1f8861fc2732067c2c1df4c88231f936acddfe106d4b78678151839b(
    *,
    abort_connection: typing.Optional[builtins.bool] = None,
    check_period: typing.Optional[jsii.Number] = None,
    ignore_network_consumers: typing.Optional[builtins.bool] = None,
    max_slow_count: typing.Optional[jsii.Number] = None,
    max_slow_duration: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca913e11cc9f95a989edf8dc13ff6a8ccd2fea12cd97661b7dabb0fcd52f4e95(
    *,
    admin: typing.Optional[builtins.str] = None,
    queue: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    temp_queue: typing.Optional[builtins.bool] = None,
    temp_topic: typing.Optional[builtins.bool] = None,
    topic: typing.Optional[builtins.str] = None,
    write: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ea8d070ea58412c08a3c6c3ee54b6e5f44482e0862e9aae8b4ded60bc0963a1(
    *,
    authorization_entries: typing.Optional[typing.Sequence[IAuthorizationMapAuthorizationEntry]] = None,
    default_entry: typing.Optional[IAuthorizationMapDefaultEntry] = None,
    temp_destination_authorization_entry: typing.Optional[TempDestinationAuthorizationEntry] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36be44b87e5caee82a19a320bc7247a9d0420edb55e86d554041ac7c9a40f0c5(
    *,
    authorization_map: typing.Optional[IAuthorizationPluginMap] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33236241482e941c1050a0a4182e06a7e8c310b6b3c03d31f08168915c49c5e4(
    *,
    advisory_support: typing.Optional[builtins.str] = None,
    allow_temp_auto_creation_on_send: typing.Optional[builtins.bool] = None,
    anonymous_producer_advisory_support: typing.Optional[builtins.bool] = None,
    cache_temp_destinations: typing.Optional[builtins.bool] = None,
    consumer_system_usage_portion: typing.Optional[jsii.Number] = None,
    dedicated_task_runner: typing.Optional[builtins.bool] = None,
    delete_all_messages_on_startup: typing.Optional[builtins.str] = None,
    keep_durable_subs_active: typing.Optional[builtins.bool] = None,
    max_purged_destinations_per_sweep: typing.Optional[jsii.Number] = None,
    monitor_connection_splits: typing.Optional[builtins.bool] = None,
    offline_durable_subscriber_task_schedule: typing.Optional[jsii.Number] = None,
    offline_durable_subscriber_timeout: typing.Optional[jsii.Number] = None,
    persistence_thread_priority: typing.Optional[jsii.Number] = None,
    persistent: typing.Optional[builtins.str] = None,
    populate_jmsx_user_id: typing.Optional[builtins.bool] = None,
    producer_system_usage_portion: typing.Optional[jsii.Number] = None,
    reject_durable_consumers: typing.Optional[builtins.bool] = None,
    rollback_only_on_async_exception: typing.Optional[builtins.bool] = None,
    schedule_period_for_destination_purge: typing.Optional[jsii.Number] = None,
    scheduler_support: typing.Optional[builtins.str] = None,
    split_system_usage_for_producers_consumers: typing.Optional[builtins.bool] = None,
    start: typing.Optional[builtins.bool] = None,
    system_usage: typing.Optional[builtins.str] = None,
    task_runner_priority: typing.Optional[jsii.Number] = None,
    time_before_purge_temp_destinations: typing.Optional[jsii.Number] = None,
    use_authenticated_principal_for_jmsx_user_id: typing.Optional[builtins.bool] = None,
    use_mirrored_queues: typing.Optional[builtins.bool] = None,
    use_temp_mirrored_queues: typing.Optional[builtins.bool] = None,
    use_virtual_dest_subs: typing.Optional[builtins.bool] = None,
    use_virtual_dest_subs_on_creation: typing.Optional[builtins.bool] = None,
    use_virtual_topics: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417062601f86bee8c4fd23717a3ff86a1fc7e55b6c213b42c4de5cecffed428f(
    *,
    destination_interceptors: typing.Optional[typing.Sequence[IBrokerDestinationInterceptor]] = None,
    destination_policy: typing.Optional[PolicyMap] = None,
    destinations: typing.Optional[typing.Sequence[IBrokerDestination]] = None,
    network_connectors: typing.Optional[typing.Sequence[NetworkConnector]] = None,
    persistence_adapter: typing.Optional[KahaDB] = None,
    plugins: typing.Optional[typing.Sequence[IBrokerPlugin]] = None,
    system_usage: typing.Optional[SystemUsage] = None,
    transport_connectors: typing.Optional[typing.Sequence[TransportConnector]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__484fed5b2043e609169f4d2eddf970d9a21c5f322351007bdbe1fffecd9321bd(
    *,
    legacy_group_mapping: typing.Optional[builtins.bool] = None,
    queue_search_base: typing.Optional[builtins.str] = None,
    refresh_interval: typing.Optional[jsii.Number] = None,
    temp_search_base: typing.Optional[builtins.str] = None,
    topic_search_base: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c021fe2103540ddf6c5824eabf75d06071687aeb44fbc93a30f04a98bf9d7aca(
    *,
    cache_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55f192922949bc3410849c08dce90ef485834345e1972e51db7861cc2fbdf0ef(
    *,
    ptp_client_id: typing.Optional[builtins.str] = None,
    ptp_suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fea3a5eeeaebdf98b5f3858133ffc5af14ef44ab178d4ea29e326d7758188ca1(
    *,
    concurrent_send: typing.Optional[builtins.bool] = None,
    copy_message: typing.Optional[builtins.bool] = None,
    forward_only: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8cc069ee6c0e313fa768f631fb2ba39058f4bdc9b21f957d92bca5c6dd50c70(
    *,
    forward_to: typing.Optional[typing.Sequence[ICompositeQueueForwardTo]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39ee33e76b38c2d63ef5e12e7ab3c0802408439741c9b8a321a1cbc95829fc4f(
    *,
    concurrent_send: typing.Optional[builtins.bool] = None,
    copy_message: typing.Optional[builtins.bool] = None,
    forward_only: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a86f745d8984e09be513b38c446cd680a0cc985dd78ca34dda7c22dc9d1a01e(
    *,
    forward_to: typing.Optional[typing.Sequence[ICompositeTopicForwardTo]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6513d9e9ea3daa5e567f8a8394b3bdac49855004f4e18422af302cf8c2f826(
    *,
    rate_duration: typing.Optional[jsii.Number] = None,
    rate_limit: typing.Optional[jsii.Number] = None,
    replay_delay: typing.Optional[jsii.Number] = None,
    replay_when_no_consumers: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc6fff10dc8874486da7c565aa124d27a595cbcd48fa6e84c155d110f8ac8a3f(
    *,
    limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2cbd128c8c9c8c2a065b7fc59d7dd95f6f731ee12bb144058cdf95553d33365(
    *,
    dead_letter_queue: typing.Optional[builtins.str] = None,
    enable_audit: typing.Optional[builtins.bool] = None,
    expiration: typing.Optional[jsii.Number] = None,
    max_audit_depth: typing.Optional[jsii.Number] = None,
    max_producers_to_audit: typing.Optional[jsii.Number] = None,
    process_expired: typing.Optional[builtins.bool] = None,
    process_non_persistent: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d10da1babb28c5d2891fc6ec89b793eb63fbd35fc3e68dae569219b835c658(
    *,
    drop_all: typing.Optional[builtins.bool] = None,
    drop_only: typing.Optional[builtins.str] = None,
    drop_temporary_queues: typing.Optional[builtins.bool] = None,
    drop_temporary_topics: typing.Optional[builtins.bool] = None,
    report_interval: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50fa0228dec4d45f18f78f29cee3a8505f39f80e7aa031d8efeec64233a74aa5(
    *,
    queue: typing.Optional[builtins.str] = None,
    selector: typing.Optional[builtins.str] = None,
    topic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7adb44d41d8e49fcbb46ef92514c621a67cb332f291d6c9ae4a09310e948996e(
    *,
    maximum_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a9b5917136dc09decbf89720beebac050e6eeb81ea26144d2cc51b9252209d(
    *,
    maximum_size: typing.Optional[jsii.Number] = None,
    use_shared_buffer: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738246b0909f76598acb4b4b2b6a1297c150d6820aad0e923260d22e59c430d9(
    *,
    persistence_flag: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396a1855177dac2190dfdd51d8590562a113154098f59346dd92adbd08db8b3e(
    *,
    destination_per_durable_subscriber: typing.Optional[builtins.bool] = None,
    enable_audit: typing.Optional[builtins.bool] = None,
    expiration: typing.Optional[jsii.Number] = None,
    max_audit_depth: typing.Optional[jsii.Number] = None,
    max_producers_to_audit: typing.Optional[jsii.Number] = None,
    process_expired: typing.Optional[builtins.bool] = None,
    process_non_persistent: typing.Optional[builtins.bool] = None,
    queue_prefix: typing.Optional[builtins.str] = None,
    queue_suffix: typing.Optional[builtins.str] = None,
    topic_prefix: typing.Optional[builtins.str] = None,
    topic_suffix: typing.Optional[builtins.str] = None,
    use_queue_for_queue_messages: typing.Optional[builtins.bool] = None,
    use_queue_for_topic_messages: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37d74e2c8f6462c9caa8fbd30b74bed2016110347400f38513b7d43726af521f(
    *,
    checkpoint_interval: typing.Optional[jsii.Number] = None,
    concurrent_store_and_dispatch_queues: typing.Optional[builtins.bool] = None,
    index_write_batch_size: typing.Optional[jsii.Number] = None,
    journal_disk_sync_interval: typing.Optional[jsii.Number] = None,
    journal_disk_sync_strategy: typing.Optional[JournalDiskSyncStrategy] = None,
    preallocation_strategy: typing.Optional[PreallocationStrategy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4903e0e6089df5869a8182bbd41239c9eac8673cc37b35745b5833ac94659e6(
    *,
    percent_of_jvm_heap: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__095bcde135ae2bb2629ace626440c4dfd7fa593b2c59e0d1fe863eed4f69960d(
    *,
    bucket_count: typing.Optional[jsii.Number] = None,
    cache_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0987f07067169dcc392adce7a9a113038b882f4b48f5fdef1c06814eab139f6b(
    *,
    copy_message: typing.Optional[builtins.bool] = None,
    postfix: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ef8c92a358ac4ca23a18ff5996168f92d5b918c0dbd16ae115f0f3e51ae8a91(
    *,
    advisory_ack_percentage: typing.Optional[jsii.Number] = None,
    advisory_for_failed_forward: typing.Optional[builtins.bool] = None,
    advisory_prefetch_size: typing.Optional[jsii.Number] = None,
    always_sync_send: typing.Optional[builtins.bool] = None,
    bridge_factory: typing.Optional[builtins.str] = None,
    bridge_temp_destinations: typing.Optional[builtins.bool] = None,
    broker_name: typing.Optional[builtins.str] = None,
    broker_url: typing.Optional[builtins.str] = None,
    check_duplicate_messages_on_duplex: typing.Optional[builtins.bool] = None,
    client_id_token: typing.Optional[builtins.str] = None,
    conduit_network_queue_subscriptions: typing.Optional[builtins.bool] = None,
    conduit_subscriptions: typing.Optional[builtins.bool] = None,
    connection_filter: typing.Optional[builtins.str] = None,
    consumer_priority_base: typing.Optional[jsii.Number] = None,
    consumer_ttl: typing.Optional[jsii.Number] = None,
    decrease_network_consumer_priority: typing.Optional[builtins.bool] = None,
    destination_filter: typing.Optional[builtins.str] = None,
    dispatch_async: typing.Optional[builtins.bool] = None,
    duplex: typing.Optional[builtins.bool] = None,
    dynamic_only: typing.Optional[builtins.bool] = None,
    gc_destination_views: typing.Optional[builtins.bool] = None,
    gc_sweep_time: typing.Optional[jsii.Number] = None,
    local_uri: typing.Optional[builtins.str] = None,
    message_ttl: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    network_ttl: typing.Optional[jsii.Number] = None,
    object_name: typing.Optional[builtins.str] = None,
    prefetch_size: typing.Optional[builtins.str] = None,
    static_bridge: typing.Optional[builtins.bool] = None,
    suppress_duplicate_queue_subscriptions: typing.Optional[builtins.bool] = None,
    suppress_duplicate_topic_subscriptions: typing.Optional[builtins.bool] = None,
    sync_durable_subs: typing.Optional[builtins.bool] = None,
    uri: typing.Optional[builtins.str] = None,
    use_broker_name_as_id_sees: typing.Optional[builtins.bool] = None,
    use_compression: typing.Optional[builtins.bool] = None,
    user_name: typing.Optional[builtins.str] = None,
    use_virtual_dest_subs: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f7ad0a20e0a79768282f7582ba222192e38500452723755a8aeefdd97cf99e5(
    *,
    durable_destinations: typing.Optional[typing.Sequence[INetworkConnectorDurableDestination]] = None,
    dynamically_included_destinations: typing.Optional[typing.Sequence[INetworkConnectorDynamicallyIncludedDestination]] = None,
    excluded_destinations: typing.Optional[typing.Sequence[INetworkConnectorExcludedDestination]] = None,
    statically_included_destinations: typing.Optional[typing.Sequence[INetworkConnectorStaticallyIncludedDestination]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348e1aac7b1b3a19d35c65856b1eb8b3c476e977b88ec7f2ebf7b3fa67cb554d(
    *,
    evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49631d6f710fba8e428a2e8ac209a3468ad03fc65737c8eceb7c5769312c9f22(
    *,
    evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23c62a13be3fffdfc2d1295584eda7324f2e1566f73469ce4b3523eb2e2ec056(
    *,
    advisory_for_consumed: typing.Optional[builtins.bool] = None,
    advisory_for_delivery: typing.Optional[builtins.bool] = None,
    advisory_for_discarding_messages: typing.Optional[builtins.bool] = None,
    advisory_for_fast_producers: typing.Optional[builtins.bool] = None,
    advisory_for_slow_consumers: typing.Optional[builtins.bool] = None,
    advisory_when_full: typing.Optional[builtins.bool] = None,
    all_consumers_exclusive_by_default: typing.Optional[builtins.bool] = None,
    always_retroactive: typing.Optional[builtins.bool] = None,
    blocked_producer_warning_interval: typing.Optional[jsii.Number] = None,
    consumers_before_dispatch_starts: typing.Optional[jsii.Number] = None,
    cursor_memory_high_water_mark: typing.Optional[jsii.Number] = None,
    do_optimze_message_storage: typing.Optional[builtins.bool] = None,
    durable_topic_prefetch: typing.Optional[jsii.Number] = None,
    enable_audit: typing.Optional[builtins.bool] = None,
    expire_messages_period: typing.Optional[jsii.Number] = None,
    gc_inactive_destinations: typing.Optional[builtins.bool] = None,
    gc_with_network_consumers: typing.Optional[builtins.bool] = None,
    inactive_timeout_before_gc: typing.Optional[jsii.Number] = None,
    inactive_timout_before_gc: typing.Optional[jsii.Number] = None,
    include_body_for_advisory: typing.Optional[builtins.bool] = None,
    lazy_dispatch: typing.Optional[builtins.bool] = None,
    max_audit_depth: typing.Optional[jsii.Number] = None,
    max_browse_page_size: typing.Optional[jsii.Number] = None,
    max_destinations: typing.Optional[jsii.Number] = None,
    max_expire_page_size: typing.Optional[jsii.Number] = None,
    max_page_size: typing.Optional[jsii.Number] = None,
    max_producers_to_audit: typing.Optional[jsii.Number] = None,
    max_queue_audit_depth: typing.Optional[jsii.Number] = None,
    memory_limit: typing.Optional[builtins.str] = None,
    message_group_map_factory_type: typing.Optional[builtins.str] = None,
    minimum_message_size: typing.Optional[jsii.Number] = None,
    optimized_dispatch: typing.Optional[builtins.bool] = None,
    optimize_message_store_in_flight_limit: typing.Optional[jsii.Number] = None,
    persist_jms_redelivered: typing.Optional[builtins.bool] = None,
    prioritized_messages: typing.Optional[builtins.bool] = None,
    producer_flow_control: typing.Optional[builtins.bool] = None,
    queue: typing.Optional[builtins.str] = None,
    queue_browser_prefetch: typing.Optional[jsii.Number] = None,
    queue_prefetch: typing.Optional[jsii.Number] = None,
    reduce_memory_footprint: typing.Optional[builtins.bool] = None,
    send_advisory_if_no_consumers: typing.Optional[builtins.bool] = None,
    store_usage_high_water_mark: typing.Optional[jsii.Number] = None,
    strict_order_dispatch: typing.Optional[builtins.bool] = None,
    temp_queue: typing.Optional[builtins.bool] = None,
    temp_topic: typing.Optional[builtins.bool] = None,
    time_before_dispatch_starts: typing.Optional[jsii.Number] = None,
    topic: typing.Optional[builtins.str] = None,
    topic_prefetch: typing.Optional[jsii.Number] = None,
    use_cache: typing.Optional[builtins.bool] = None,
    use_consumer_priority: typing.Optional[builtins.bool] = None,
    use_prefetch_extension: typing.Optional[builtins.bool] = None,
    use_topic_subscription_inflight_stats: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b16a938162f792e6f035ab637529ca7ab2155f46a84e5ebb7ecdcb401142d82c(
    *,
    dead_letter_strategy: typing.Optional[IPolicyEntryDeadLetterStrategy] = None,
    destination: typing.Optional[IPolicyEntryDestination] = None,
    dispatch_policy: typing.Optional[IPolicyEntryDispatchPolicy] = None,
    message_eviction_strategy: typing.Optional[IPolicyEntryMessageEvictionStrategy] = None,
    message_group_map_factory: typing.Optional[IPolicyEntryMessageGroupMapFactory] = None,
    network_bridge_filter_factory: typing.Optional[ConditionalNetworkBridgeFilterFactory] = None,
    pending_durable_subscriber_policy: typing.Optional[IPolicyEntryPendingDurableSubscriberPolicy] = None,
    pending_message_limit_strategy: typing.Optional[IPolicyEntryPendingMessageLimitStrategy] = None,
    pending_queue_policy: typing.Optional[IPolicyEntryPendingQueuePolicy] = None,
    pending_subscriber_policy: typing.Optional[IPolicyEntryPendingSubscriberPolicy] = None,
    slow_consumer_strategy: typing.Optional[IPolicyEntrySlowConsumerStrategy] = None,
    subscription_recovery_policy: typing.Optional[IPolicyEntrySubscriptionRecoveryPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce613069539bf302c4cdee3cd46342316ebc47bb4e02daf50547a701ef7fbd29(
    *,
    default_entry: typing.Optional[PolicyEntry] = None,
    policy_entries: typing.Optional[typing.Sequence[PolicyEntry]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc6a31f34c1ca729699b2e5e65f940317bdd647631da7b5c49a03f9ad05f4d47(
    *,
    multiplier: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520edbc8a2e4d132d95ebe20421298a7d5cdb1697ef3e391029deae70ba9d22c(
    *,
    query: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045a61d5c821ac7d87c756a997288dc98ba7614227b1f8e03a255a27c764f623(
    *,
    dlq: typing.Optional[builtins.bool] = None,
    physical_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0c06cf42b3a16ae312438524e15ab844665cfdade59df885a2d8c79090c62a4(
    *,
    fallback_to_dead_letter: typing.Optional[builtins.bool] = None,
    send_to_dlq_if_max_retries_exceeded: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36395bd5901ad6ac98438f1fc43289f3d11c59fa5c04643683667d111c50f07(
    *,
    redelivery_policy_map: typing.Optional[RedeliveryPolicyMap] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6077886a71c12977282d30fc5f0b51f19aae5ac7885822c2a50f7a35528f2ba3(
    *,
    back_off_multiplier: typing.Optional[jsii.Number] = None,
    collision_avoidance_percent: typing.Optional[jsii.Number] = None,
    initial_redelivery_delay: typing.Optional[jsii.Number] = None,
    maximum_redeliveries: typing.Optional[jsii.Number] = None,
    maximum_redelivery_delay: typing.Optional[jsii.Number] = None,
    pre_dispatch_check: typing.Optional[builtins.bool] = None,
    queue: typing.Optional[builtins.str] = None,
    redelivery_delay: typing.Optional[jsii.Number] = None,
    temp_queue: typing.Optional[builtins.bool] = None,
    temp_topic: typing.Optional[builtins.bool] = None,
    topic: typing.Optional[builtins.str] = None,
    use_collision_avoidance: typing.Optional[builtins.bool] = None,
    use_exponential_back_off: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb2ba699d1c8d6e98011cdf67a67e81d54863850137e50644259c74430e4feb1(
    *,
    default_entry: typing.Optional[RedeliveryPolicy] = None,
    redelivery_policy_entries: typing.Optional[typing.Sequence[RedeliveryPolicy]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0453478659ff4daa1aa92da51caa58f8bb3b0ccaf13faf912c640a7f4d6b3f9a(
    *,
    wrapped: typing.Optional[IRetainedMessageSubscriptionRecoveryPolicyWrapped] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f87807482f477573540ab9243bf742280b9611fc889ba8c3c9f9c6f311efc4a(
    *,
    enable_audit: typing.Optional[builtins.bool] = None,
    expiration: typing.Optional[jsii.Number] = None,
    max_audit_depth: typing.Optional[jsii.Number] = None,
    max_producers_to_audit: typing.Optional[jsii.Number] = None,
    process_expired: typing.Optional[builtins.bool] = None,
    process_non_persistent: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f63014b243db8d09966f65c9a1dea54fca5915ea5a8cfca673bede4dcf8cf59f(
    *,
    dead_letter_queue: typing.Optional[ISharedDeadLetterStrategyDeadLetterQueue] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__593afe7700b49120eeacfdc39f20b1737c31e796cf5c0fba83340dabeef3f38c(
    *,
    immediate_priority_dispatch: typing.Optional[builtins.bool] = None,
    use_cache: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0376a5d92919815b5da10fc9118724a951cc73c3fa2f4558445606e509c6fc8(
    *,
    send_fail_if_no_space: typing.Optional[builtins.bool] = None,
    send_fail_if_no_space_after_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4350699e0199c9c74281c8e4a718389b7996a7b013c831ac023d780de0519611(
    *,
    memory_usage: typing.Optional[MemoryUsage] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__095b0872f3a3448d73eb4d8e7ad935cbbc66c8a59d882a9f21dc0bd8418589d2(
    *,
    admin: typing.Optional[builtins.str] = None,
    queue: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    temp_queue: typing.Optional[builtins.bool] = None,
    temp_topic: typing.Optional[builtins.bool] = None,
    topic: typing.Optional[builtins.str] = None,
    write: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78e7c188346ee36d099526b16714598cf80f5e8576d2eb36c6c543d3ecfa835d(
    *,
    dlq: typing.Optional[builtins.bool] = None,
    physical_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6a3d63d19b7ccaf3a3be05b53ee63eb3f97fbb929cbf05474afecf829c9dfb(
    *,
    dlq: typing.Optional[builtins.bool] = None,
    physical_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a51728b5cffbed4dddb97fa340ac96b66764c7a34eafa7b0dd53e9b4d4233cf(
    *,
    future_only: typing.Optional[builtins.bool] = None,
    process_network_messages: typing.Optional[builtins.bool] = None,
    ttl_ceiling: typing.Optional[jsii.Number] = None,
    zero_expiration_override: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2182c1329a941a479e79d04f110f2c1edc4e3f3fd1cca777ace1e909336a589(
    *,
    recover_duration: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16300f6db82cccf9a732d65ed21ce94e15b6b1c333c7fbe72776903eebff319f(
    *,
    dlq: typing.Optional[builtins.bool] = None,
    physical_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7baea1cf102b98da3ea85cc1e67aa836d7d8df137de74c177a25fc41240c3ff(
    *,
    name: typing.Optional[Protocol] = None,
    rebalance_cluster_clients: typing.Optional[builtins.bool] = None,
    update_cluster_clients: typing.Optional[builtins.bool] = None,
    update_cluster_clients_on_remove: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08109f7f0746dc91f300f10996517ff42b15d1de294910e8d359b9d495ad77ea(
    *,
    evict_expired_messages_high_watermark: typing.Optional[jsii.Number] = None,
    property_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63aa66ce16f478861859efa0e94b3fca2a0b743b4732997ce7616882ba25b086(
    *,
    virtual_destinations: typing.Sequence[IVirtualDestinationInterceptorVirtualDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7248d19f987267d0f2e2a874b04e72d00a9f08f457a4135c2d60773e385ba2e5(
    *,
    concurrent_send: typing.Optional[builtins.bool] = None,
    local: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
    postfix: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    selector_aware: typing.Optional[builtins.bool] = None,
    transacted_send: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8321b03ee93c02e7e07dfd82974dd0f3ce3ade6e8bdd528c0877ec782b6d5c4(
    *,
    attrs_names_overrides: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elems_names_overrides: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    tag_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b86807a21059632c4ecda964b38deac635d4925a9efc4d3abec2d74eb47f6049(
    attributes: typing.Optional[typing.Union[BrokerAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    *,
    destination_interceptors: typing.Optional[typing.Sequence[IBrokerDestinationInterceptor]] = None,
    destination_policy: typing.Optional[PolicyMap] = None,
    destinations: typing.Optional[typing.Sequence[IBrokerDestination]] = None,
    network_connectors: typing.Optional[typing.Sequence[NetworkConnector]] = None,
    persistence_adapter: typing.Optional[KahaDB] = None,
    plugins: typing.Optional[typing.Sequence[IBrokerPlugin]] = None,
    system_usage: typing.Optional[SystemUsage] = None,
    transport_connectors: typing.Optional[typing.Sequence[TransportConnector]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38d361ae6f5af7a0fa988e81490664c79fe9c06331383ebe19dd631e901d6133(
    attributes: typing.Optional[typing.Union[CompositeQueueAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    *,
    forward_to: typing.Optional[typing.Sequence[ICompositeQueueForwardTo]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__533ac9d1b4aa6b766e74ceb0cbd1e24b2574bd8c5cd63b4c3743697abb5c842b(
    attributes: typing.Optional[typing.Union[CompositeTopicAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    *,
    forward_to: typing.Optional[typing.Sequence[ICompositeTopicForwardTo]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c8209e37f7ad27ae3038be0302d136b5e39e2cc94a82b2f86589e72832bdf60(
    attributes: typing.Optional[typing.Union[NetworkConnectorAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    *,
    durable_destinations: typing.Optional[typing.Sequence[INetworkConnectorDurableDestination]] = None,
    dynamically_included_destinations: typing.Optional[typing.Sequence[INetworkConnectorDynamicallyIncludedDestination]] = None,
    excluded_destinations: typing.Optional[typing.Sequence[INetworkConnectorExcludedDestination]] = None,
    statically_included_destinations: typing.Optional[typing.Sequence[INetworkConnectorStaticallyIncludedDestination]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974fb4dd1e99e08ccb1cb147c121753b9ff7c54f03b0a10b55e053414e5d72dc(
    attributes: typing.Optional[typing.Union[PolicyEntryAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    *,
    dead_letter_strategy: typing.Optional[IPolicyEntryDeadLetterStrategy] = None,
    destination: typing.Optional[IPolicyEntryDestination] = None,
    dispatch_policy: typing.Optional[IPolicyEntryDispatchPolicy] = None,
    message_eviction_strategy: typing.Optional[IPolicyEntryMessageEvictionStrategy] = None,
    message_group_map_factory: typing.Optional[IPolicyEntryMessageGroupMapFactory] = None,
    network_bridge_filter_factory: typing.Optional[ConditionalNetworkBridgeFilterFactory] = None,
    pending_durable_subscriber_policy: typing.Optional[IPolicyEntryPendingDurableSubscriberPolicy] = None,
    pending_message_limit_strategy: typing.Optional[IPolicyEntryPendingMessageLimitStrategy] = None,
    pending_queue_policy: typing.Optional[IPolicyEntryPendingQueuePolicy] = None,
    pending_subscriber_policy: typing.Optional[IPolicyEntryPendingSubscriberPolicy] = None,
    slow_consumer_strategy: typing.Optional[IPolicyEntrySlowConsumerStrategy] = None,
    subscription_recovery_policy: typing.Optional[IPolicyEntrySubscriptionRecoveryPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09aa41f17317e87dd1259cff1522c4036fa95063d6b25f969749b491e7490e79(
    attributes: typing.Optional[typing.Union[RedeliveryPluginAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    *,
    redelivery_policy_map: typing.Optional[RedeliveryPolicyMap] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c961dc576afdf1ca90429c3cb3a32260094088dd8a9b977c7c2ac5e2525d92d(
    attributes: typing.Optional[typing.Union[SharedDeadLetterStrategyAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    *,
    dead_letter_queue: typing.Optional[ISharedDeadLetterStrategyDeadLetterQueue] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba34c1586ba6070c23266ec12af9620b7284fdae61c7df8795e6a4d53a29d33(
    attributes: typing.Optional[typing.Union[SystemUsageAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    *,
    memory_usage: typing.Optional[MemoryUsage] = None,
) -> None:
    """Type checking stubs"""
    pass
